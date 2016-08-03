import time
import os
import time
from time import sleep
import pymysql
import datetime
from datetime import timedelta

CONST_DB = "letturePezziDB"
CONST_NUM_PC_TOT_DAY = 403

class logicCounter():

    def __init__(self):
        self.db_conn = None
        self.num_pieces_until_now = 0
        self.daily_qty = 0
        self.pieces_x_hour = 0
        self.db_conn = pymysql.connect("localhost", "root", "sardegna", CONST_DB)
        self.set_daily_qty()
        if self.db_conn is None:
            raise

    def __del__(self):
        if self.db_conn is not None:
            self.db_conn.close()

    def add_piece_in_hour(self):
        curr_date = datetime.datetime.now().strftime('%Y-%m-%d')
        curr_time = datetime.datetime.now().strftime('%H:%M:%S')

        cursor = self.db_conn.cursor()
        s_qry = "SELECT iOraId, tOraIni, tOraFine FROM TOra_Orari WHERE tOraIni <= '%s' AND tOraFine >= '%s'" \
                %(datetime.datetime.now().strftime("%H:%M:%S"), datetime.datetime.now().strftime("%H:%M:%S"))
        cursor.execute(s_qry)
        row_orari = cursor.fetchone()
        if row_orari is not None:
            hour_found = True
            # Hour record exists. Searching for TLet_Letture record. If not found inserting...
            s_qry = "SELECT * FROM TLet_Letture WHERE dLetDataLettura = '%s' AND tLetOraIni <= '%s' AND tLetOraFine >= '%s'" \
                %(datetime.datetime.now().strftime("%Y-%m-%d"), datetime.datetime.now().strftime("%H:%M:%S"),
                  datetime.datetime.now().strftime("%H:%M:%S"))
            cursor.execute(s_qry)
            row = cursor.fetchone()
            id_let = 0

            if row is not None:
                id_let = int(row[0])
                s_qry = "UPDATE TLet_Letture SET iLetNumProg = %d WHERE iLetId = %d" %(self.get_pieces_until_now() + 1, id_let)
            else:
                s_qry = "INSERT INTO TLet_Letture set dLetDataLettura = '%s', sLetNote = '', tLetOraini = '%s', tLetOraFine = '%s', iLetNumProg = %d" \
                        % (curr_date, (datetime.datetime.min + row_orari[1]).time().strftime("%H:%M:%S"),
                           (datetime.datetime.min + row_orari[2]).time().strftime("%H:%M:%S"),
                           self.get_pieces_until_now() + 1)

            cursor.execute(s_qry)
            self.db_conn.commit()
        else:
            hour_found = False
        return hour_found

    def get_pieces_until_now(self):
        cursor = self.db_conn.cursor()
        s_qry = "select SUM(iLetNumProg) from TLet_Letture where dLetDataLettura = '%s'" %datetime.datetime.now().strftime("%Y-%m-%d")
        cursor.execute(s_qry)
        row = cursor.fetchone()
        if row[0] is not None:
            self.num_pieces_until_now = int(row[0])
        else:
            self.num_pieces_until_now = 0
        return self.num_pieces_until_now

    def get_pieces_this_hour(self):
        cursor = self.db_conn.cursor()
        s_qry = "select iLetNumProg from TLet_Letture where dLetDataLettura = '%s' and tLetOraIni <= '%s' and tLetOraFine >= '%s' "\
                % (datetime.datetime.now().strftime("%Y-%m-%d"), datetime.datetime.now().strftime("%H:%M:%S"),
                   datetime.datetime.now().strftime("%H:%M:%S"))
        cursor.execute(s_qry)
        row = cursor.fetchone()
        if row[0] is not None:
            return row[0]
        else:
            return 0

    def get_hours(self):
        s_qry = "SELECT iOraId, tOraIni, tOraFine, fOraTotPezzi FROM TOra_Orari ORDER BY tOraIni"
        cursor = self.db_conn.cursor()
        cursor.execute(s_qry)
        row = cursor.fetchone()

        i_count = 1
        hour_list = []
        while row is not None:
            dict_orari = dict()
            dict_orari["ID"] = row[0]
            tm_from= datetime.datetime.strptime(row[1].__str__(), "%H:%M:%S").strftime("%H:%M")
            tm_to = datetime.datetime.strptime(row[2].__str__(), "%H:%M:%S").strftime("%H:%M")
            dict_orari["ORARIO"] = "%s - %s" %(tm_from, tm_to)
            if row[3] is not None:
                dict_orari["qty"] = row[3]
            else:
                dict_orari["qty"] = 0

            hour_list.append(dict_orari)
            i_count += 1
            row = cursor.fetchone()
        cursor.close()
        return hour_list

    def set_daily_qty(self, qta=0):
        cursor = self.db_conn.cursor()
        if qta == 0:
            s_qry = "SELECT SUM(fOraTotPezzi) FROM TOra_Orari"
            cursor.execute(s_qry)
            qta = int(cursor.fetchone()[0])
            if qta ==0:
                qta = CONST_NUM_PC_TOT_DAY

        if qta != self.daily_qty:
            s_qry = "SELECT iTimId FROM TTim_TotaleImpostati WHERE dTimData = '%s'" %datetime.datetime.now().strftime("%Y-%m-%d")
            cursor.execute(s_qry)
            row = cursor.fetchone()
            if row is not None:
                s_qry_upd = "UPDATE TTim_TotaleImpostati set iTimQta = %d where iTimId = %d" %(qta, row[0])
            else:
                s_qry_upd = "INSERT INTO TTim_TotaleImpostati set dTimData = '%s', iTimQta = %d" %(datetime.datetime.now().strftime("%Y-%m-%d"), qta)
            cursor.execute(s_qry_upd)
            self.db_conn.commit()
            self.daily_qty = qta

        s_qry = "SELECT count(*) FROM TOra_Orari order by tOraIni"
        cursor.execute(s_qry)
        hours_total = int(cursor.fetchone()[0])
        self.pieces_x_hour = qta // hours_total


    def get_daily_qty(self):
        return self.daily_qty


