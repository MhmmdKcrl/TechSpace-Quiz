### TechSpace-Quiz

## Tapşırıq 1

1. Mysql və Adminer servisleri olan docker-compose faylı yaradın.
2. Adminer'da MySQL databazasına qoşulun
3. Movie_info adlı cədvəl yaradın. (CREATE funksiyası ilə)
4. Cədvəldə id, title, released, director, genre sütunları olmalıdır.
5. 'id' PRIMARY KEY, AUTO_INCREMENT, datatipi isə ədəd olmalıdır.
6. 'title' NULL olmamalıdır, datatipi isə character olmalıdır.
7. 'released' tarix olmalıdır.
8. 'director' boş olmamalıdır, datatip isə character olmalıdır.
10. 'genre' character olmalıdır.


### Important

* Kodunuzun və cədvəlinizin ekran görüntüsünü çəkin, onu bu qovluğa əlavə edin.


## Tapşırıq 2: Film məlumatlarını alın və databazada saxlayın
# Məqsəd: OMDB API-dən film məlumatlarını almaq və pymysql istifadə edərək MySQL verilənlər bazasında saxlamaq üçün requests modulundan istifadə edin.

- Təlimatlar:
1. Virtual environment yaradın
2. Requests pip paketini quraşdırın
3. Pip paketlərini requirements.txt faylına dondurun
4. * 1ci hissə. Datanı inputdan əldə edin:

    OMDB API-dən məlumat əldə etmək üçün sorğu modulundan istifadə edin.
    Nümunə API çağırışı: http://www.omdbapi.com/?t=Inception&apikey=your_api_key

    APİ KEY - '5d9df2b8'

    title, released, genre, director kimi müvafiq sahələri çıxarın.

    Əgər daxil edilən film mövcud deyilsə, uygun mesajı print'ə çıxarın.

4. * 2ci hissə. Məlumatı saxla:

    pymysql istifadə edərək MySQL verilənlər bazasına qoşulun.
    Task 1'dəki cədvələ alınmış film məlumatlarını daxil edin.