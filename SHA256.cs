using System;
using System.Globalization;
using System.IO;

using System.Threading;
using System.Net.Security;
using System.Text;
using System.Linq;

namespace Test
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter word > ");
            string urmom = Console.ReadLine();
            urmom = SHA256(urmom);
            Console.ReadLine();
        }

        static string SHA256(string password)
        {
            //Converting password to Binary
            byte[] bytes = Encoding.ASCII.GetBytes(password);
            string binary = string.Join("", bytes.Select(byt => Convert.ToString(byt, 2).PadLeft(8, '0')));

            int msg_length = binary.Length;
            string big_endian = Convert.ToString(msg_length,2);

            // Adding Padding (first 16 chunks)
            int padding = 512 - msg_length - 1 - big_endian.Length;
            string pads = new string('0', padding);
            string chunk_16 = binary.Substring(0, Math.Min(binary.Length, 32));
            string msg_binary = binary + "1" + pads + big_endian + chunk_16;

            // Creating 64 chunks Array 
            string[] chunks = new string[64];
            string empty_chunk = "00000000000000000000000000000000";

            // Adding first 16 Chunks
            for (int i = 0; 16 > i; i++)
            {
                
                int n = 32 * i;
                string chunk = "";
                for (int j = 0; 32 > j; j++)
                {
                    try
                    {
                        chunk += msg_binary[n + j];
                    }
                    catch
                    {
                        chunk += "0";
                    }
                    
                }
                chunks[i] = chunk;
            }
            // Filling rest of the chunks
            for (int i = 16; i < 64; i++)
            {
                chunks[i] = empty_chunk;
            }

            // Calculating chunks
            for (int i = 16; 64 > i; i++)
            {
                string sig_1 = sigmoid(chunks[i - 15], 7, 18, 3);
                string sig_2 = sigmoid(chunks[i - 2], 17, 19, 10);

                int row_1 = Convert.ToInt32(chunks[i - 16], 2);
                int row_2 = Convert.ToInt32(chunks[i - 7], 2);
                int Sig_1 = Convert.ToInt32(sig_1, 2);
                int Sig_2 = Convert.ToInt32(sig_2, 2);
                //Ensure string hits 32 bits
                string new_chunk = Convert.ToString(row_1+row_2+Sig_1+Sig_2,2);
                
                chunks[i] = bits_32(new_chunk);
            }

            //The first 32 Bits of the fractional value of the square root of the first 64 prime numbers.
            string[] K_constants = 
            {
                "01000010100010100010111110011000", 
                "01110001001101110100010010010001", 
                "10110101110000001111101111001111",
                "11101001101101011101101110100101", 
                "00111001010101101100001001011011", 
                "01011001111100010001000111110001", 
                "10010010001111111000001010100100", 
                "10101011000111000101111011010101", 
                "11011000000001111010101010011000", 
                "00010010100000110101101100000001", 
                "00100100001100011000010110111110", 
                "01010101000011000111110111000011", 
                "01110010101111100101110101110100",  
                "10000000110111101011000111111110", 
                "10011011110111000000011010100111", 
                "11000001100110111111000101110100", 
                "11100100100110110110100111000001", 
                "11101111101111100100011110000110", 
                "00001111110000011001110111000110", 
                "00100100000011001010000111001100", 
                "00101101111010010010110001101111", 
                "01001010011101001000010010101010", 
                "01011100101100001010100111011100", 
                "01110110111110011000100011011010", 
                "10011000001111100101000101010010", 
                "10101000001100011100011001101101", 
                "10110000000000110010011111001000", 
                "10111111010110010111111111000111", 
                "11000110111000000000101111110011", 
                "11010101101001111001000101000111", 
                "00000110110010100110001101010001", 
                "00010100001010010010100101100111", 
                "00100111101101110000101010000101", 
                "00101110000110110010000100111000", 
                "01001101001011000110110111111100", 
                "01010011001110000000110100010011", 
                "01100101000010100111001101010100", 
                "01110110011010100000101010111011", 
                "10000001110000101100100100101110", 
                "10010010011100100010110010000101", 
                "10100010101111111110100010100001", 
                "10101000000110100110011001001011", 
                "11000010010010111000101101110000", 
                "11000111011011000101000110100011", 
                "11010001100100101110100000011001", 
                "11010110100110010000011000100100", 
                "11110100000011100011010110000101", 
                "00010000011010101010000001110000", 
                "00011001101001001100000100010110", 
                "00011110001101110110110000001000", 
                "00100111010010000111011101001100", 
                "00110100101100001011110010110101", 
                "00111001000111000000110010110011", 
                "01001110110110001010101001001010", 
                "01011011100111001100101001001111", 
                "01101000001011100110111111110011", 
                "01110100100011111000001011101110", 
                "01111000101001010110001101101111", 
                "10000100110010000111100000010100", 
                "10001100110001110000001000001000", 
                "10010000101111101111111111111010", 
                "10100100010100000110110011101011", 
                "10111110111110011010001111110111", 
                "11000110011100010111100011110010"

            };

            string h0 = "01101010000010011110011001100111";
            string h1 = "10111011011001111010111010000101";
            string h2 = "00111100011011101111001101110010";
            string h3 = "10100101010011111111010100111010";
            string h4 = "01010001000011100101001001111111";
            string h5 = "10011011000001010110100010001100";
            string h6 = "00011111100000111101100110101011";
            string h7 = "01011011111000001100110100011001";


            string a = bits_32(h0);
            string b = bits_32(h1);
            string c = bits_32(h2);
            string d = bits_32(h3);
            string e = bits_32(h4);
            string f = bits_32(h5);
            string g = bits_32(h6);
            string h = bits_32(h7);


            for (int i = 0;i<64;i++)
            {
                string Sigma_0 = sigma(e, 6, 11, 25);
                string Sigma_1 = sigma(a, 2, 13, 22);
                string choice = choose(e, f, g);
                string Majority = majority(a,b,c);
                string temp1 = Convert.ToString((Convert.ToInt32(h,2) + Convert.ToInt32(Sigma_0,2) + Convert.ToInt32(choice,2) + Convert.ToInt32(K_constants[i],2) + Convert.ToInt32(chunks[i],2)),2);
                string temp2 = Convert.ToString((Convert.ToInt32(Sigma_1,2) + Convert.ToInt32(Majority,2)),2);

                h = g;
                g = f; 
                f = e;
                e = bits_32(Convert.ToString((Convert.ToInt32(d, 2) + Convert.ToInt32(temp1, 2)), 2));
                d = c;
                c = b;
                b = a;
                a = bits_32(Convert.ToString((Convert.ToInt32(temp1, 2) + Convert.ToInt32(temp2, 2)), 2));
            }


            h0 = (Convert.ToInt32(h0, 2) + Convert.ToInt32(a, 2)).ToString("X");
            
            h1 = (Convert.ToInt32(h1, 2) + Convert.ToInt32(b, 2)).ToString("X");
            h2 = (Convert.ToInt32(h2, 2) + Convert.ToInt32(c, 2)).ToString("X");
            h3 = (Convert.ToInt32(h3, 2) + Convert.ToInt32(d, 2)).ToString("X");
            h4 = (Convert.ToInt32(h4, 2) + Convert.ToInt32(e, 2)).ToString("X");
            h5 = (Convert.ToInt32(h5, 2) + Convert.ToInt32(f, 2)).ToString("X");
            h6 = (Convert.ToInt32(h6, 2) + Convert.ToInt32(g, 2)).ToString("X");
            h7 = (Convert.ToInt32(h7, 2) + Convert.ToInt32(h, 2)).ToString("X");

            string digest = h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7;

           return digest;
        }

        static string bits_32(string chunk)
        {
            
            for (int n = 0; n < 32; n++)
            {
                if (chunk.Length == 32)
                {
                    break;
                }
                else
                {
                    chunk = "0" + chunk;
                }
            }
            return chunk;
        }
        static string sigmoid(string chunk, int right_rotate_1, int right_rotate_2, int right_shift)
        {

            //Rotate Chunks
            string chunk_1 = chunk.Substring(32 - right_rotate_1, right_rotate_1) + chunk.Substring(0, 32 - right_rotate_1);
            string chunk_2 = chunk.Substring(32 - right_rotate_2, right_rotate_2) + chunk.Substring(0, 32 - right_rotate_2);
            string temp = new string('0', right_shift);
            //Shift Chunks
            string chunk_3 = temp + chunk.Substring(0, 32 - right_shift);
            string new_chunk = "";
            for (int i=0; i < 32; i++)
            {
                {
                    //XOR gates
                    bool a = (chunk_1[i] == '1');
                    bool b = (chunk_2[i] == '1');
                    bool c = (chunk_3[i] == '1');
                    switch(((a && b && c ) || (a && !b && !c )) || ((!a && b && !c) || (!a && !b && c)))
                    {
                        case true: new_chunk += "1";break;
                        case false: new_chunk += "0"; break;
                    }
                }
            }
           return new_chunk;
        }
        static string choose(string e, string f, string g)
        {
            string new_e = "";
            for (int i = 0;e.Length>i;i++)
            {
                switch (e[i])
                {
                    case '0': new_e += g[i];break;
                    case '1': new_e += f[i];break;
                }
            }
           
            return new_e;
        }
        static string sigma(string chunk, int right_rotate_1, int right_rotate_2, int right_rotate_3)
        {
            //Rotate
            string chunk_1 = chunk.Substring(32 - right_rotate_1, right_rotate_1) + chunk.Substring(0, 32 - right_rotate_1);
            string chunk_2 = chunk.Substring(32 - right_rotate_2, right_rotate_2) + chunk.Substring(0, 32 - right_rotate_2);
            string chunk_3 = chunk.Substring(32 - right_rotate_3, right_rotate_3) + chunk.Substring(0, 32 - right_rotate_3);
        
            string new_chunk = "";
            for (int i = 0; i < 32; i++)
            {
                {
                    //XOR gates
                    bool a = (chunk_1[i] == '1');
                    bool b = (chunk_2[i] == '1');
                    bool c = (chunk_3[i] == '1');
                    switch (((a && b && c) || (a && !b && !c)) || ((!a && b && !c) || (!a && !b && c)))
                    {
                        case true: new_chunk += "1"; break;
                        case false: new_chunk += "0"; break;
                    }
                }
            }
            return new_chunk;
        }
        static string majority(string a, string b, string c)
        {
            string Majority = "";
            int vote,a_1,b_1,c_1;
            for(int i = 0; i < a.Length; i++)
            {
                a_1 = a[i] - '0';
                b_1 = b[i] - '0';
                c_1 = c[i] - '0';
                vote = a_1 + b_1 + c_1;
                if (vote < 2)
                {
                    Majority += "0";
                }
                else if (vote > 1)
                {
                    Majority += "1";
                }
            }
            return Majority;
        }
    }
}
