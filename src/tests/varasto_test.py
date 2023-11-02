import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus(self):
        self.varasto = Varasto(-100)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)
    
    def test_negatiivinen_saldo(self):
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_alku_saldo_enemman_kuin_tilavuus(self):
        self.varasto = Varasto(10, 20)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_lisataan_negatiivinen_maara(self):
        # lähtotilanne saldossa 10
        self.varasto = Varasto(10, 20)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_lisataan_yli_varaston_kapasiteetin(self):
        # lähtotilanne saldossa 10
        self.varasto = Varasto(10, 20)
        self.varasto.lisaa_varastoon(1)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_otetaan_negatiivinen_maara(self):
        self.varasto = Varasto(10, 20)
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_jos_otetaan_enemman_kuin_saldo_palautetaan_kokonaissaldo(self):
        # lähtotilanne saldossa 10
        self.varasto = Varasto(10, 20)
        self.varasto.ota_varastosta(200)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_str_palauttaa_saldon_ja_tilavuuden(self):
        self.varasto = Varasto(10, 20)
        string = "saldo = 10, vielä tilaa 0"
        return_value = str(self.varasto)
        self.assertAlmostEqual(return_value, string)





        

