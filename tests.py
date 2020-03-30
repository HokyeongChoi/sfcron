import unittest
import sqlite3
import pandas as pd
from pandas.testing import assert_frame_equal

from final_auto_crawling_db_update import filter_festival, is_similar

class TestFilter(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        cur = self.con.cursor()
        cur.execute('create table "festival_info" ("festival_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "축제명" varchar(200) NOT NULL, "개최지역" varchar(200) NOT NULL, "개최기간" varchar(200) NOT NULL);')

        cur.execute('insert into festival_info values (?, ?, ?, ?)', ('1', '축제1', '지역1', '기간1'))
        cur.execute('insert into festival_info values (?, ?, ?, ?)', ('2', '축제2', '지역2', '기간2'))
        cur.execute('insert into festival_info values (?, ?, ?, ?)', ('3', '축제3', '지역3', '기간3'))

        cur.close()

        d = {
            'title': ['축제1', '축제2'],
            '개최지역': ['지역1', '지역4'],
            '개최기간': ['기간1', '기간4'],
        }
        self.df_festival = pd.DataFrame(data=d)
    
    def tearDown(self):
        self.con.close()

    def test_filter_festival(self):
        df_filtered = filter_festival(self.df_festival, self.con)
        expected = pd.DataFrame(data={
            'title': ['축제2'],
            '개최지역': ['지역4'],
            '개최기간': ['기간4'],
        })
        assert_frame_equal(df_filtered, expected)

class TestSequenceMatcher(unittest.TestCase):

    def setUp(self):
        con = sqlite3.connect("SEOUL_FESTIVAL.db")
        cur = con.cursor()

        cur.execute('SELECT 축제장소 FROM festival_info;')
        self.locs = tuple(row[0] for row in cur)

        con.close()

    def test_214_266_207_271(self):
        cnt = 0
        for loc in self.locs:
            cnt += 1
            if is_similar(loc, '석촌호수 수변무대(동, 서호), 서울놀이마당'):
                self.assertIn(cnt, (214, 266))
            if is_similar(loc, '서울 종로구 아르코예술극장 소극장 등'):
                self.assertIn(cnt, (207, 271))

if __name__ == '__main__':
    unittest.main()