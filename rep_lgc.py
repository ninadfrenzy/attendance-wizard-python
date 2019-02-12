import camelot
import pandas as pd
import csv
import fpdf
import sqlite3 as sql
import matplotlib.pyplot as plt
from PyPDF2 import PdfFileWriter, PdfFileReader
import smtplib 
import os

def flush():
	os.remove('attendance.db')
def add_to_db(user,password):
	connection_object=sql.connect('security.db')
	cursor = connection_object.cursor()
	values = (user,password,)
	cursor.execute('INSERT INTO users values(?,?)',values)
	connection_object.commit()
	cursor.execute('SELECT id FROM users WHERE id=? AND pass=?',values)
	re = cursor.fetchone()
	if(re):
		print("suceess")
	else:
		print("fail")


def authenticate(user,password):
	connection_object=sql.connect('security.db')
	cursor = connection_object.cursor()
	values = (user,password,)
	cursor.execute('SELECT id FROM users WHERE id=? AND pass=?',values)
	results = cursor.fetchone()
	if(results):
		return True
	else:
		return False

def clean_data(file_name,sub_list):
	count=0
	#pages has to be in form '1,2,...n'
	infile = PdfFileReader(file_name, 'rb')
	output = PdfFileWriter()
	formatted_str_pages=''
	pages=0
	for i in range(infile.getNumPages()):
		p = infile.getPage(i)
		if len(p.extractText())>100:
         # getContents is None if  page is blank
			output.addPage(p)
			pages=pages+1
			formatted_str_pages = formatted_str_pages+str(pages)+','

	formatted_str_pages = formatted_str_pages[0:len(formatted_str_pages)-1]

	tables = camelot.read_pdf(file_name, pages=formatted_str_pages)
	tables = tables[1:]
	frames = []
	for table in tables:
		frames.append(table.df)
	cnt=0
	for index,row in tables[0].df.iterrows():
		if '01' in row[0]:
			break
		else:
			cnt = cnt+1

	new_data_frame = pd.concat(frames).iloc[cnt:]
	new_data_frame.columns = sub_list
	for col in new_data_frame.columns:
		pd.to_numeric(new_data_frame[col],errors='coerce')



	total_list = new_data_frame.iloc[-1].tolist()
	#new_data_frame = new_data_frame[:-1]
	
	new_data_frame.fillna(0,inplace = True)
	total_list=total_list[2:]
	total_list = list(map(str,total_list))
	cols=new_data_frame.columns.tolist()
	cols=cols[2:]
	empty_list=list()
	for i in range(len(cols)):
		empty_list.append("\n"+cols[i]+"\t-->\t")
		empty_list.append(total_list[i])
	total_str = "".join(empty_list)
	#new_data_frame.corr(method='pearson').to_csv('corr.csv')
	return new_data_frame,total_str


def get_from_db(table_name,connection):
	data_frame=pd.read_sql('select * from '+table_name,connection)
	del data_frame['index']
	total_list = data_frame.iloc[-1].tolist()
	#new_data_frame = new_data_frame[:-1]
	total_list=total_list[2:]
	total_list = list(map(str,total_list))
	cols=data_frame.columns.tolist()
	cols=cols[2:]
	empty_list=list()
	for i in range(len(cols)):
		empty_list.append("\n"+cols[i]+"\t-->\t")
		empty_list.append(total_list[i])
	total_str = "".join(empty_list)
	
	return data_frame,total_str


def create_connection():
	connection_object=sql.connect('attendance.db')
	return connection_object


def store_data(data_frame,table_name) :

	connection_object=sql.connect('attendance.db')
	data_frame.to_sql(table_name,con=connection_object,if_exists='replace')
	return connection_object
    #top5 = pd.read_sql('sw_listect name,total from '+TableName+' order by total desc limit 5 ',con = connection_object)


def find_irregulars(tb,data_frame,connection):
	data_frame=data_frame[:-1]
	sub_defaulters = list()
	#con_object = sql.connect('att.db')
	for index,row in data_frame.iterrows():
		row_list=row.tolist()

		row_list=row_list[2:-3]
		row_list = list(map(float,row_list))
		label_list=data_frame.columns.tolist()
		label_list=label_list[2:-3]
		for i in range(len(row_list)):
			if(row_list[i]<75):
				sub_defaulters.append([row['name'],label_list[i],row_list[i]])
	f = lambda x: "\t\t\t".join(map(str,x))
	sub_defaulters_str ="\n".join(f(x) for x in sub_defaulters)
	crsr=connection.cursor()
	crsr.execute("select rollno,name,total from "+tb+" where total<75 and total <>100")
	res=crsr.fetchall()
	f = lambda x: "\t\t\t".join(map(str,x))
	defaulters_str ="\n".join(f(x) for x in res)
	crsr.execute("select rollno,name,total from "+tb+" where total between 75 and 80")
	res=crsr.fetchall()
	f = lambda x: "\t\t\t".join(map(str,x))
	warnings_str ="\n".join(f(x) for x in res)
	return defaulters_str,warnings_str,sub_defaulters_str


def top_five(data_frame):
	data_frame=data_frame[:-1]
	def sort_fn(x):
		return x[1]
	top_list=list()
	total_list=data_frame['total'].tolist()
	setlist=list(set(total_list))
	setlist = list(map(float,setlist))
	setlist=sorted(setlist,reverse=True)
	setlist = setlist[0:5]
	
	for i,row in data_frame.iterrows():
		if(float(row['total']) in setlist):
			top_list.append([row['name'],row['total']])  
		
	temp = (sorted(top_list,key=sort_fn,reverse=True))
	
	f = lambda x: "\t\t\t\t".join(map(str,x))
	five_str ="\n".join(f(x) for x in temp)
	
	return five_str


def most_bunked_sub(data_frame):
	total_list = data_frame.iloc[-1].tolist()
	data_frame=data_frame[:-1]
	cols=data_frame.columns.tolist()
	cols = cols[2:-3]
	total_list = total_list[2:-3]
	total_list = list(map(float,total_list))
	subject_list = [[cols[i],total_list[i]] for i in range(len(cols))]
	most_bunked=(min(subject_list,key=lambda x: x[1]))
	most_bunked=[item for item in most_bunked]
	most_bunked=list(map(str,most_bunked))
	most_bunked=" ".join(most_bunked)
	return most_bunked


def data_querying(connection,name,rno,table_name):
	con_crsr = connection.cursor()
	
	if(len(name)!=0):
		name="%"+name+"%"
		tup=(name,)
		con_crsr.execute('select * from '+table_name+' where name like ?',tup)
		
	else:
		rno="%"+rno
		tup=(rno,)
		con_crsr.execute('select * from '+table_name+' where rollno like ?',tup)
	data=con_crsr.fetchone()
	data=[value for value in data]
	data=data[1:]
	labels=[item[0] for item in con_crsr.description]
	labels=labels[1:]
	labelled_data=list()
	for i in range(len(labels)):
		labelled_data.append([labels[i],data[i]])
		#labelled_data.append(data[i])
	#labelled_data=list(map(str,labelled_data))
	#labelled_data=" ".join(labelled_data)
	f = lambda x: "\t\t\t".join(map(str,x))
	labelled_data ="\n".join(f(x) for x in labelled_data)
	labelled_data="\n\n________________________________________________________\n\n"+labelled_data+"\n\n"
	con_crsr.close()
	return labelled_data		


def division_graph(data_frame) :
	total = data_frame.iloc[-1].tolist()
	total = total[2:-3]
	cols = data_frame.columns.tolist()
	cols = cols[2:-3]
	total = list(map(float,total))
	plt.bar(cols,total)
	plt.title("division_graph")
	plt.show()


def stud_wise_graph(data_frame,rn,name,connection,table_name):
	data_frame=data_frame[:-1]
	if(len(rn)!=0):
		crsr=connection.cursor()
		rn="%"+rn
		tup=(rn,)
		crsr.execute("select rollno from "+table_name+" where rollno like ?",tup)
		roll=crsr.fetchone()
		roll="".join(roll)
	else:
		crsr=connection.cursor()
		name="%"+name+"%"
		tup=(name,)
		crsr.execute("select rollno from "+table_name+" where name like ?",tup)
		roll=crsr.fetchone()
		roll="".join(roll)

	labellist=data_frame.columns.tolist()
	#print(labellist)
	

	individual=data_frame.where(data_frame['rollno'] == roll).dropna()
	individual = [x.tolist() for y,x in individual.iterrows()]
	individual = individual[0]
	
	#division_graph(individual)
	
	labellist=labellist[2:-3]
	individual = individual[2:-3]
	individual = list(map(float,individual))
	plt.title("stud_wise_graph")
	plt.bar(labellist,individual)

	plt.show()


def save_as_pdf(data,file_name):

	#pdf=fpdf.FPDF(format='letter')
	#pdf.add_page()
	#pdf.set_font("arial",size=12)
	#for item in data:
		#pdf.write(5,str(item))
	#pdf.output(filename)
	if file_name:
		pdf=fpdf.FPDF(format='letter')
		pdf.add_page()
		pdf.set_font("Arial",size=12)
		for i in data:
			pdf.write(5,str(i))
		pdf.output(file_name)
		pdf.close()


def range_attendance(start,end,connection,table_name):
	con_crsr = connection.cursor()
	con_crsr.execute('select rollno,name,total from '+table_name+' where total between '+str(start)+' and '+str(end))
	fetched=con_crsr.fetchall()
	f = lambda x: " ".join(map(str,x))
	in_between ="\n".join(f(x) for x in fetched)
	in_between="\n\n______________________________________________________\n\n"+in_between
	return in_between


def mail_students(connection,table_name,user,pwd,filename):
	crsr=connection.cursor()
	crsr.execute("select rollno from "+table_name+" where total<75")
	res=crsr.fetchall()
	res=[value for item in res for value in item]
	mailing_file=open(filename,'r')
	mailing_file=csv.reader(mailing_file)
	me=user
	if(len(user)!=0 and len(pwd)!=0):
		
		if(smtplib.SMTP('smtp.gmail.com', 587)):
			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.starttls()
			s.login(user,pwd)
		else:
			print("cannot connect")
	
	for row in mailing_file:
		#print(row)
		if(row[0] in res):

			crsr.execute('select name,total from '+table_name+' where rollno="'+row[0]+'"')
			val=crsr.fetchone()
			val=[item for item in val]
			message="Dear "+val[0]+",\n attendance is really  bad  only "+str(val[1])+"percent"
			you=row[1]
			
			s.sendmail(me,you, message)
	s.quit()


def correlate(data_frame):
	data_frame=data_frame[:-1]
	correlation_frame=data_frame.corr(method='pearson')
	correlation_list=correlation_frame['total'].tolist()
	labels=data_frame.columns.tolist()
	labels=labels[2:]
	correlation_list=[[labels[i],correlation_list[i]] for i in range(len(correlation_list))]
	correlation_list=correlation_list[:-4]
	correlation_list=sorted(correlation_list,reverse=True,key=lambda x:x[1])
	
	rel_message=("The attendance report suggests that the impact of "+correlation_list[0][0]+","+correlation_list[1][0]+" and "+correlation_list[2][0]
	+" has been significant on the total attendance")
	return rel_message


def counting(connection,table_name):
	crsr=connection.cursor()
	tup = (table_name,)
	crsr.execute('select count(*) from t1 where total<75.0')
	num_def=crsr.fetchone()
	num_def=[str(item) for item in num_def]
	crsr.execute('select count(*) from '+table_name+' where total between 75 and 80')
	num_war=crsr.fetchone()
	num_war=[str(item) for item in num_war]
	crsr.execute('select count(*) from '+table_name+' where aoa<75 or cn<75 or dbms<75 or sd<75 or isee<75 or sepm<75 or toc<75 or cnl<75 or dbmsl<75 or sdl<75')
	num_subdef=crsr.fetchone()
	num_subdef=[str(item) for item in num_subdef]
	return "".join(num_def),"".join(num_subdef),"".join(num_war)

	
	


