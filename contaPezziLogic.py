import time
import os
import time
from time import sleep
import pymysql
import datetime
from datetime import timedelta
from PyQt5 import QtWidgets

CONST_DB = "letturePezziDB"
CONST_NUM_PC_TOT_DAY = 403

class logicCounter():

    def __init__(self, parent):
        self.parent = parent
        self.db_conn = None
        #self.num_pieces_until_now = 0
        self.daily_qty = 0
        self.pieces_x_hour = 0
        self.db_conn = pymysql.connect("localhost", "root", "sardegna", CONST_DB)
        self.set_daily_qty()
        self.minutePassed = datetime.datetime.now().strftime("%M")
        self.prev_preview_pcs = 0
        if self.db_conn is None:
            raise

    def __del__(self):
        if self.db_conn is not None:
            self.db_conn.close()

    def add_piece_in_hour(self):
        curr_date = datetime.datetime.now().strftime('%Y-%m-%d')
        # curr_time = datetime.datetime.now().strftime('%H:%M:%S')

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
                s_qry = "UPDATE TLet_Letture SET iLetNumProg = %d WHERE iLetId = %d" %(self.get_pieces_this_hour()[0] + 1, id_let)
            else:
                s_qry = "INSERT INTO TLet_Letture set dLetDataLettura = '%s', sLetNote = '', tLetOraini = '%s', tLetOraFine = '%s', iLetNumProg = %d" \
                        % (curr_date, (datetime.datetime.min + row_orari[1]).time().strftime("%H:%M:%S"),
                           (datetime.datetime.min + row_orari[2]).time().strftime("%H:%M:%S"), 1)

            cursor.execute(s_qry)
            self.db_conn.commit()
        else:
            hour_found = False
        return hour_found

    def get_pieces_until_now(self):
        cursor = self.db_conn.cursor()
        s_qry = "select SUM(iLetNumProg), iLetId from TLet_Letture where dLetDataLettura = '%s'" %datetime.datetime.now().strftime("%Y-%m-%d")
        cursor.execute(s_qry)
        row = cursor.fetchone()
        if (row is not None) and (row[0] is not None):
            num_pieces_until_now = int(row[0])
        else:
            num_pieces_until_now = 0

        return num_pieces_until_now

    def get_pieces_this_hour(self):
        result = []
        cursor = self.db_conn.cursor()
        s_qry = "select iLetNumProg from TLet_Letture where dLetDataLettura = '%s' and tLetOraIni <= '%s' and tLetOraFine >= '%s' "\
                % (datetime.datetime.now().strftime("%Y-%m-%d"), datetime.datetime.now().strftime("%H:%M:%S"),
                   datetime.datetime.now().strftime("%H:%M:%S"))
        cursor.execute(s_qry)
        row = cursor.fetchone()
        if row[0] is not None:
            result.append(row[0])
        else:
            result.append(0)
        s_qry = "select iOraId from TOra_Orari where tOraIni <= '%s' AND tOraFine >= '%s'" \
                %(datetime.datetime.now().strftime("%H:%M:%S"), datetime.datetime.now().strftime("%H:%M:%S"))
        cursor.execute(s_qry)
        row = cursor.fetchone()
        if row[0] is not None:
            result.append(row[0])
        else:
            result.append(0)

        return result

    def get_preview_pieces_this_hour(self, tm_start, tm_end):
        s_qry = "SELECT fOraTotPezzi FROM TOra_Orari WHERE tOraIni <= '%s' AND tOraFine >= '%s'" \
            %(tm_start, tm_end)
        #% (datetime.datetime.now().strftime("%H:%M:%S"), datetime.datetime.now().strftime("%H:%M:%S"))
        cursor = self.db_conn.cursor()
        cursor.execute(s_qry)
        row = cursor.fetchone()
        if (row is not None) and (row[0] is not None):
            return int(row[0])
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
            dict_orari["HOUR_START"] = "%s" %tm_from
            dict_orari["HOUR_END"] = "%s" %tm_to
            if row[3] is not None:
                dict_orari["qty_expected"] = row[3]
            else:
                dict_orari["qty_expected"] = 0

            s_qry_pcs_in_hour = "SELECT iLetNumProg FROM TLet_Letture WHERE dLetDataLettura = '%s' AND " \
                                " tLetOraIni <= '%s' AND tLetOraFine >= '%s'" %(datetime.datetime.now().strftime("%Y-%m-%d"), row[1], row[2])

            cur_pcs_in_hour = self.db_conn.cursor()
            cur_pcs_in_hour.execute(s_qry_pcs_in_hour)
            row_pcs = cur_pcs_in_hour.fetchone()
            if row_pcs is not None:
                dict_orari["qty_hour"] = row_pcs[0]
            else:
                dict_orari["qty_hour"] = 0

            dict_orari["label_pcs_done"] = QtWidgets.QLabel(self.parent.ui.qfFatti)

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

    def get_preview_pcs_till_now(self, do_anyway=False):
        minute_now = datetime.datetime.now().strftime("%M")
        if (minute_now != self.minutePassed) | do_anyway:
            self.minutePassed = datetime.datetime.now().strftime("%M")
            cursor = self.db_conn.cursor()
            now = datetime.datetime.now() - timedelta(hours=1)
            old_time = now.strftime('%H:%M:%S')
            curr_time = datetime.datetime.now().strftime('%H:%M:%S')

            sQry = "SELECT sum(fOraTotPezzi) FROM TOra_Orari WHERE tOraIni < '%s'" % old_time
            cursor.execute(sQry)
            tot_prec = cursor.fetchone()

            sQry = "SELECT fOraTotPezzi FROM TOra_Orari WHERE (tOraIni <= '%s') and (tOraFine > '%s') " \
                   %(curr_time, curr_time)
            cursor.execute(sQry)
            prev_now = cursor.fetchone()
            if prev_now != None:
                tot_actual = (prev_now[0] * float(self.minutePassed)) // 60.0

                if tot_prec != None:
                    if tot_prec[0] != None:
                        self.prev_preview_pcs = tot_prec[0] + tot_actual
                        return int(self.prev_preview_pcs)
                    else:
                        self.prev_preview_pcs = tot_actual
                        return int(self.prev_preview_pcs)
            else:
                return int(self.prev_preview_pcs)

            cursor.close()
        else:
            return int(self.prev_preview_pcs)



