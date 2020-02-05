import unittest
import sqlite3
import pandas as pd
from pandas.testing import assert_frame_equal

from final_auto_crawling_db_update import filter_festival

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
            '축제명': ['축제1', '축제2'],
            '개최지역': ['지역1', '지역4'],
            '개최기간': ['기간1', '기간4'],
        }
        self.df_festival = pd.DataFrame(data=d)
    
    def tearDown(self):
        self.con.close()

    def test_filter_festival(self):
        df_filtered = filter_festival(self.df_festival, self.con)
        expected = pd.DataFrame(data={
            '축제명': ['축제2'],
            '개최지역': ['지역4'],
            '개최기간': ['기간4'],
        })
        assert_frame_equal(df_filtered, expected)

if __name__ == '__main__':
    unittest.main()