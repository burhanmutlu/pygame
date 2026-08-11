using System;

class Program
{
    private static string alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ";
    static void Main()
    {
        string gizliMesaj;
        int k = 3;
        string sifreliMesaj, cozulmusMesaj;
        string mod;
        Console.WriteLine("Sezar şifreleme algoritması\n");
        Console.Write("1 - şifrele 2 - şifre çöz 3 - çıkış: ");
        mod = Console.ReadLine();
        
        if (mod == "1")
        {
            gizliMesaj = Console.ReadLine();
            Console.WriteLine($"(GİZLİ MESAJ):{gizliMesaj}");
            sifreliMesaj = Sifrele(gizliMesaj, k);
            Console.WriteLine($"(SİFRELENMİS MESAJ) : {sifreliMesaj}");
            
        }

        if (mod == "2")
        {
            gizliMesaj = Console.ReadLine();
            Console.WriteLine($"(GİZLİ MESAJ):{gizliMesaj}");
            cozulmusMesaj = Coz(gizliMesaj, k);
            Console.WriteLine($"(COZULMUS MESAJ) : {cozulmusMesaj}");
        }

        if (mod == "3")
        {
            Environment.Exit(0);
        }
    }


    static string Sifrele(string gizliMesaj, int k)
    {
        gizliMesaj=gizliMesaj.ToUpper();

        string sonuc = "";

        for (int baslangic = 0; baslangic < gizliMesaj.Length; baslangic++)
        {
            char suAnkiHarf = gizliMesaj[baslangic];
            int mevcutSira = alfabe.IndexOf(suAnkiHarf);

            if (mevcutSira != -1)
            {
                int yeniSira = (mevcutSira + k)%alfabe.Length;
                sonuc += alfabe[yeniSira];
            }
            else
            {
                sonuc += suAnkiHarf;
            }
        }
        return sonuc;
    }

    static string Coz(string sifreliMesaj, int k)
    {
        sifreliMesaj=sifreliMesaj.ToUpper();

        string sonuc = "";

        for (int baslangic = 0; baslangic < sifreliMesaj.Length; baslangic++)
        {
            char suAnkiHarf = sifreliMesaj[baslangic];
            int mevcutSira = alfabe.IndexOf(suAnkiHarf);

            if (mevcutSira != -1)
            {
                int yeniSira = (mevcutSira - k + alfabe.Length)%alfabe.Length;
                sonuc += alfabe[yeniSira];
            }
            else
            {
                sonuc += suAnkiHarf;
            }
        }
        return sonuc;
    }
}