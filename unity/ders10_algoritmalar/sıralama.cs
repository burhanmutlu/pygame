using System;
class Program
{
    static void Main()
    {
        int[] sayilar = {32,54,100,89,34,65,54,34,12,1,34,34,54,100};
        Console.Write("İLK: ");
        foreach (int sayi in sayilar) Console.Write($"{sayi} ");
        Console.WriteLine();
        for (int i = 0; i < sayilar.Length - 1; i ++)
        {
            for (int j = 0; j < sayilar.Length-1; j++)
            {
                if (sayilar[j] > sayilar[j + 1])
                {
                    int temp = sayilar[j];
                    sayilar[j] = sayilar[j + 1];
                    sayilar[j + 1] = temp;
                }
            }
            Console.Write($"{i+1}. DURUM: ");
            foreach (int sayi in sayilar) Console.Write($"{sayi} ");
            Console.WriteLine();
        }
        Console.Write("SON: ");
        foreach (int sayi in sayilar) Console.Write($"{sayi} ");
        
    }
}