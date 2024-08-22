## TechSpace-Quiz

# Tapşırıq 1

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

* Kodunuzun və cədvəlinizin ekran görüntüsünü çəkin, onu task1 qovluğuna əlavə edin.


# Tapşırıq 2: Film məlumatlarını alın və databazada saxlayın
### Məqsəd: OMDB API-dən film məlumatlarını requests modulundan istifadə edib almaq və pymysql istifadə edərək MySQL verilənlər bazasında saxlamaq.

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


# Tapşırıq 3

1. Flask proyekti yaradılmalıdır
2. Proyektə SQLAlchemy quraşdırılmalıdır
3. Movie modeli düzəldilməlidir (fildlər: id, title, released, director, genre)
4. Databazaya 6 fərqli film məlumatları daxil edilməlidir. (insert)
5. 1 route olmalıdır ('/movies/') və əlavə dinamik route yaradılmalıdır. ('/movies/<int:movie_id>') (movie.html)
6. Flaskı run etdikdə, 'http://127.0.0.1:5000/movies/' path-ində index.html səhifəsi açılmalıdır.
7. İndex səhifəsində render funksiyasında Movie modelinin bütün obyektləri çağırılaraq template-ə göndərilməlidir.
8. Template-də jinja vasitəsi ilə bütün kitablar ekrana çıxarılmalıdır. (for loop)
9. Template folderində movie.html adında yeni fayl yaradılmalıdır.
10. Bu faylda film haqqında bütün məlumatlar render zamanı dinamik dəyişəcək.
11. Movie.html səhifəsində filmin adı, rejissoru, janrı, buraxilis ili, route-un funksiyasından gəlməlidir və jinja ilə template-ə yərləşdirilməlidir.



