''' Nhóm 07 KHDL16A1
NGUYỄN BÁ DUY ANH
LÊ VIẾT GIÁP
ĐỒNG KHẮC KIÊN
PHAN ĐỨC HIẾU TRUNG
PHẠM ANH TÚ
'''
import os 
import csv
path='files/ds_mat_hang.csv'
lstHangHoa=[]
# Hàm thứ nhất
def mo_file_csv(path,lstHangHoa):
    f=open(path,'w',encoding='utf-8')
    csv.writer(f).writerow(['Mã hàng','Tên mặt hàng','Đơn vị tính','Đơn giá','Số lượng','Thành tiền'])
    for i in lstHangHoa:
        csv.writer(f).writerow([i['Mã hàng'],i['Tên mặt hàng'],i['Đơn vị tính'],i['Đơn giá'],i['Số lượng'],i['Thành tiền']])
    f.close()
    return
# Hàm thứ hai
def doc_file_csv(path,lstHangHoa):
    f=open(path,'r',encoding='utf-8')
    for row in csv.reader(f):
        print(row)
    f.close()
    return

# Hàm thứ ba
def nhap(lstHangHoa):
        ma_hang=input("Nhập mã hàng:")
        ten_hang=input("Nhập tên hàng:")
        dv_tinh=input("Nhập đơn vị tính:")
        don_gia=float(input("Nhập đơn giá:"))
        so_luong=int(input("Nhập số lượng:"))
        thanh_tien=don_gia*so_luong
        lstHangHoa.append({'Mã hàng':ma_hang,'Tên mặt hàng':ten_hang,'Đơn vị tính':dv_tinh,'Đơn giá':don_gia,'Số lượng':so_luong,'Thành tiền':thanh_tien})

# Hàm thứ tư
def them_hang_hoa(lstHangHoa):
    while True:
        ma_hang=input("Nhập mã hàng:")
        ten_hang=input("Nhập tên hàng:")
        dv_tinh=input("Nhập đơn vị tính:")
        don_gia=float(input("Nhập đơn giá:"))
        so_luong=int(input("Nhập số lượng:"))
        thanh_tien=don_gia*so_luong
        lstHangHoa.append({'Mã hàng':ma_hang,'Tên mặt hàng':ten_hang,'Đơn vị tính':dv_tinh,'Đơn giá':don_gia,'Số lượng':so_luong,'Thành tiền':thanh_tien})
        ctinue=int(input("Chọn 1 để tiếp tục, khác 1 để dừng"))
        if ctinue!=1:
            break

# Hàm thứ năm
def in_ds_hang_hoa(lstHangHoa):
    print('{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}'.format('Mã hàng','Tên mặt hàng','Đơn vị tính','Đơn giá','Số lượng','Thành tiền'))
    for ch in lstHangHoa:
        print('{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}'.format(ch['Mã hàng'],ch['Tên mặt hàng'],ch['Đơn vị tính'],ch['Đơn giá'],ch['Số lượng'],ch['Thành tiền']))
        
    return

# Hàm thứ sáu
def tra_cuu_hang_hoa(lstHangHoa):
    find=(input("Nhập mã hàng cần tra cứu:"))
    for i in lstHangHoa:
        a=i['Mã hàng']
    if find == a:
        print("Mã hàng",find,"có trong danh sách")
        in_ds_hang_hoa(lstHangHoa)
    else:
        print("Không tìm thấy trong danh sách hàng hóa")


# Hàm thứ tám

def tinh_thue(lstHangHoa):
    thue=[]
    for i in lstHangHoa:
        a=i["Thành tiền"]
    thue.append(a)
    t=sum(thue)
    if t<50000000.0:
        print((t*5/100))
    else:
        print((t*10)/100)
    

        
    return

# MENU CHỨC NĂNG CẦN THỰC HIỆN
while True:
    print("CHƯƠNG TRÌNH QUẢN LÝ HÀNG HÓA SIÊU THỊ")
    print('*****************************************************')
    print("Nhấn 1 để NHẬP HÀNG HÓA")
    print("Nhấn 2 để THÊM HÀNG HÓA")
    print("Nhấn 3 để XEM DANH SÁCH HÀNG HÓA")
    print("Nhấn 4 để TRA CỨU HÀNG HÓA")
    print("Nhấn 5 để LƯU FILE CSV")
    print("Nhấn 6 để ĐỌC FILE CSV")
    print("Nhấn 7 để TÍNH THUẾ")
    choice=int(input("Chọn chức năng cần thực hiện:"))
    if choice==1:
        nhap(lstHangHoa)
        
    if choice==2:
        them_hang_hoa(lstHangHoa)
        
    if choice==3:
        print("DANH SÁCH HÀNG HÓA:")
        in_ds_hang_hoa(lstHangHoa)
        print(lstHangHoa)
           
    if choice==4:
        print("TRA CỨU HÀNG HÓA")
        tra_cuu_hang_hoa(lstHangHoa)
        
    if choice==5:
        mo_file_csv(path,lstHangHoa)       
    if choice==6:
        doc_file_csv(path,lstHangHoa)
    if choice==7:
        print("Thuế của cửa hàng là:")
        tinh_thue(lstHangHoa)



    

    
