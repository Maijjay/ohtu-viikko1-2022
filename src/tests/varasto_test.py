import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_konstruktori_ei_voi_luoda_virheellista_tilavuutta(self):
        varasto = Varasto(-3)
        self.assertEqual(varasto.tilavuus, 0)

    def test_konstruktori_ei_voi_luoda_virheellista_saldoa(self):
        self.varasto = Varasto(10, -2)
        self.assertEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
    
    def test_paljonko_mahtuu_palauttaa_oikean_summan(self):
        self.varasto.lisaa_varastoon(6)
        tilaa_jaljella = self.varasto.paljonko_mahtuu()
        self.assertEqual(tilaa_jaljella, 4)

    def test_varastoon_ei_voi_lisata_virheellista_maaraa(self):
        self.varasto.lisaa_varastoon(-5)
        
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_varastoon_ei_voi_lisata_tilavuutta_enempaa(self):
        self.varasto.lisaa_varastoon(15)

        saldo = self.varasto.saldo

        self.assertEqual(saldo, 10)
    
    def test_varastosta_ei_ottaa_vihreellista_maaraa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-6)
        
        self.assertEqual(self.varasto.saldo, 5)

    def test_varastosta_ei_voi_ottaa_saldoa_enemman(self):
        self.varasto.lisaa_varastoon(2)
        
        saatu_maara = self.varasto.ota_varastosta(4)

        self.assertEqual(saatu_maara, 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_ottaminen_vahentaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(3)

        self.assertEqual(self.varasto.saldo, 5)
    
    def test_str_palauttaa_oikeanlaisen_merkkijonon(self):
        self.varasto.lisaa_varastoon(4)
        self.assertEqual(self.varasto.__str__(), "saldo = 4, vielä tilaa 6")