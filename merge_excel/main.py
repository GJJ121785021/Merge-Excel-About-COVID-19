import xlsxwriter


# 写excel
def write_excel():
    workbook = xlsxwriter.Workbook('chat.xlsx')  # 创建一个excel文件
    worksheet = workbook.add_worksheet(u'sheet1')  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1

    worksheet.set_column('A:A', 20)  # 设置第一列宽度为20像素
    bold = workbook.add_format({'bold': True})  # 设置一个加粗的格式对象

    worksheet.write('A1', 'HELLO')  # 在A1单元格写上HELLO
    worksheet.write('A2', 'WORLD', bold)  # 在A2上写上WORLD,并且设置为加粗
    worksheet.write('B2', U'中文测试', bold)  # 在B2上写上中文加粗

    worksheet.write(2, 0, 32)  # 使用行列的方式写上数字32,35,5
    worksheet.write(3, 0, 35.5)  # 使用行列的时候第一行起始为0,所以2,0代表着第三行的第一列,等价于A4
    worksheet.write(4, 0, '=SUM(A3:A4)')  # 写上excel公式
    workbook.close()


# 读
def read_excel():
    # coding=utf-8

    import xlrd

    # 打开文件
    data = xlrd.open_workbook('tmp.xlsx')

    # 查看工作表
    data.sheet_names()
    print("sheets：" + str(data.sheet_names()))

    # 通过文件名获得工作表,获取工作表1
    table = data.sheet_by_index(0)

    # 打印data.sheet_names()可发现，返回的值为一个列表，通过对列表索引操作获得工作表1
    # table = data.sheet_by_index(0)

    # 获取行数和列数
    # 行数：table.nrows
    # 列数：table.ncols
    print("总行数：" + str(table.nrows))
    print("总列数：" + str(table.ncols))

    # 获取整行的值 和整列的值，返回的结果为数组
    # 整行值：table.row_values(start,end)
    # 整列值：table.col_values(start,end)
    # 参数 start 为从第几个开始打印，
    # end为打印到那个位置结束，默认为none
    print("整行值：" + str(table.row_values(0)))
    print("整列值：" + str(table.col_values(1)))

    # 获取某个单元格的值，例如获取B3单元格值
    cel_B3 = table.cell(3, 2).value
    print("第三行第二列的值：" + cel_B3)

if __name__ == '__main__':
    # 写入Excel
    # write_excel()
    # print('写入成功')

    read_excel()



"""
#! /bin/sh
if_fail(){
    [ $? -ne 0 ] && curl httpxxx && exit 1
}

cd /web && npm install && npm run build
if_fail 

cd /scr && mvn -f pom.xml dependency:copy-dependencies && mvn package
if_fail

fuser -k -n tcp 8080
BUILD_ID=DONTKILLME
cd /home && nohup java -jar fa.jar &
if fail

curl httpsuccess
"""
