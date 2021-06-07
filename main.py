
import pymysql

# DB connection 설정
conn = pymysql.connect(
    host="localhost", user="gotaek", password="gotaek", db="imdb"
)
# cursor 설정
curs = conn.cursor(pymysql.cursors.DictCursor)


def searchTitle():
    title = input('제목을 입력하세요:')
    print()
    sql = "select * from works where primarytitle like '%s'" % (title+'%')
    curs.execute(sql)
    row = curs.fetchone()
    while row:
        print("제목: %-50s\t원제: %-50s\t개봉년도: %-10d" % (
              row["primarytitle"], row["originalTitle"], row["endYear"]))
        row = curs.fetchone()
    print()


def searchActor():
    actor = input('배우 이름을 입력하세요:')
    print()
    sql = """
        select *
        from actor a, actor_known_for n, ratings r,
        (select *
        from works
        where titleType="movie")w
        where w.workId = n.workId and a.actorId = n.actorId and r.workId = w.workId and a.primaryName like '%s'
        order by r.averageRating desc
    """ % (actor+"%")
    curs.execute(sql)
    row = curs.fetchone()
    actorName = ""
    while row:
        if (row["primaryName"] != actorName):
            print()
            actorName = row["primaryName"]
            print("%s(%s)" % (actorName, row["startYear"]))
            print()

        print("\t제목: %-50s\t개봉년도: %-4d\t별점: %-4d" % (
              row["primarytitle"], row["startYear"], row["averageRating"]))
        row = curs.fetchone()
    print()


def searchDirector():
    director = input('감독 이름을 입력하세요:')
    print()
    sql = """
        select *
        from director d,director_known_for n,ratings r,
        (select *
        from works
        where titleType="movie") w
        where w.workId=n.workId and r.workId=w.workId and n.directorId=d.directorId and d.primaryname like '%s'
        order by w.startYear
    """ % (director+"%")
    curs.execute(sql)
    row = curs.fetchone()
    directorName = ""
    while row:
        if (row["primaryName"] != directorName):
            print()
            directorName = row["primaryName"]
            print("%s(%s)" % (directorName, row["startYear"]))
            print()

        print("\t제목: %-50s\t개봉년도: %-4d\t별점: %-4d" % (
              row["primarytitle"], row["startYear"], row["averageRating"]))
        row = curs.fetchone()
    print()


def searchWriter():
    writer = input('작가 이름을 입력하세요:')
    print()
    sql = """
        select *
        from writer d,writer_known_for n,ratings r,
        (select *
        from works
        where titleType="movie") w
        where w.workId=n.workId and r.workId=w.workId and n.writerId=d.writerId and d.primaryname like '%s'
        order by w.startYear
    """ % (writer+"%")
    curs.execute(sql)
    row = curs.fetchone()
    writerName = ""
    while row:
        if (row["primaryName"] != writerName):
            print()
            writerName = row["primaryName"]
            print("%s(%s)" % (writerName, row["startYear"]))
            print()

        print("\t제목: %-50s\t개봉년도: %-4d\t별점: %-4d" % (
              row["primarytitle"], row["startYear"], row["averageRating"]))
        row = curs.fetchone()
    print()
# 메인 함수


def searchGenre():
    genre = input('장르를 입력하세요:')
    print()
    sql = """
        select *
        from works w,
        (select distinct workId
        from genretable g
        where g.genre='%s') gd,ratings r
        where w.workId=gd.workId and gd.workId=w.workId and r.workId=w.workId
        order by numVotes desc;
    """ % (genre)
    curs.execute(sql)
    row = curs.fetchone()
    writerName = ""
    for i in range(10):
        print("%d. 제목: %-50s\t개봉년도: %-4d\t별점: %-4d\t리뷰 수:%-4d" % (
              i+1, row["primarytitle"], row["startYear"], row["averageRating"], row["numVotes"]))
        row = curs.fetchone()
    print()


def main():
    while True:
        print("1)제목 검색 \n2)배우 검색 \n3)감독 검색 \n4)작가 검색 \n5)장르 검색")
        option = input()
        if option == "1":
            searchTitle()
        elif option == "2":
            searchActor()
        elif option == "3":
            searchDirector()
        elif option == "4":
            searchWriter()
        elif option == "5":
            searchGenre()
        else:
            print('잘못된 값을 입력하셨습니다.')
    curs.close()
    conn.close()


if __name__ == "__main__":
    main()
