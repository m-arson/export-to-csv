import mysql.connector
import pandas as pd

db = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="bitter",
  database="db_data"
)

c = db.cursor()

date_time = []
p1_v = []
p2_v = []
p3_v = []
p4_v = []
p5_v = []
p1_c = []
p2_c = []
p3_c = []
p4_c = []
p5_c = []
p1_pf = []
p2_pf = []
p3_pf = []
p4_pf = []
p5_pf = []
c1_pn = []
c2_pn = []
c3_pn = []
c1_bl = []
c2_bl = []
c3_bl = []
temp = []
humi = []
wind_speed = []

c.execute("SELECT log, p1_v, p2_v, p3_v, p4_v, p5_v, p1_c, p2_c, p3_c, p4_c, p5_c, p1_pf, p2_pf, p3_pf, p4_pf, p5_pf, c1_pn, c2_pn, c3_pn, c1_bl, c2_bl, c3_bl, temp, humi, wind_speed FROM tb_data")
res = c.fetchall()

for r in res:
	date_time.append(r[0])
	p1_v.append(r[1])
	p2_v.append(r[2])
	p3_v.append(r[3])
	p4_v.append(r[4])
	p5_v.append(r[5])
	p1_c.append(r[6])
	p2_c.append(r[7])
	p3_c.append(r[8])
	p4_c.append(r[9])
	p5_c.append(r[10])
	p1_pf.append(r[11])
	p2_pf.append(r[12])
	p3_pf.append(r[13])
	p4_pf.append(r[14])
	p5_pf.append(r[15])
	c1_pn.append(r[16])
	c2_pn.append(r[17])
	c3_pn.append(r[18])
	c1_bl.append(r[19])
	c2_bl.append(r[20])
	c3_bl.append(r[21])
	temp.append(r[22])
	humi.append(r[23])
	wind_speed.append(r[24])


data_frame = {
	"Datetime": date_time,
	"P1 Volt": p1_v,
	"P2 Volt": p2_v,
	"P3 Volt": p3_v,
	"P4 Volt": p4_v,
	"P5 Volt": p5_v,
	"P1 Curr": p1_c,
	"P2 Curr": p2_c,
	"P3 Curr": p3_c,
	"P4 Curr": p4_c,
	"P5 Curr": p5_c,
	"P1 PF": p1_pf,
	"P2 PF": p2_pf,
	"P3 PF": p3_pf,
	"P4 PF": p4_pf,
	"P5 PF": p5_pf,
	"C1 N Person": c1_pn,
	"C2 N Person": c2_pn,
	"C3 N Person": c3_pn,
	"C1 Brig Level": c1_bl,
	"C2 Brig Level": c2_bl,
	"C3 Brig Level": c3_bl,
	"Temperature": temp,
	"Humidity": humi,
	"Wind Speed": wind_speed
}

csv_to_save = pd.DataFrame(data_frame)

if not csv_to_save.to_csv("record-data-asli.csv", index=False):
	print("Berhasil Disimpan")
else:
	print("Gagal Disimpan")
