BEGIN TRANSACTION;
CREATE TABLE training_schedule (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    date DATETIME NOT NULL,
    time TEXT NOT NULL,
    subject TEXT NOT NULL,
    room TEXT NOT NULL,
    lecturer TEXT NOT NULL
);

INSERT INTO training_schedule (id, date, time, subject, room, lecturer)

VALUES (1, '2017-07-10', '13:00-14:30; 14:40-16:10', 'История', '441', 'Беспятова Е. Б.'),
(2, '2017-10-21', '16:20-17:50; 18:00-19:30', 'Алгебра и Геометрия', '273', 'Гончар Д. Р.'),
(3, '2017-10-28', '13:00-14:30; 14:40-16:10', 'Введение в профессиональную деятельность', 'Фр, А-63', 'Жуков Д. О.'),
(4, '2017-11-11', '9:00-10:30; 10:40-12:10', 'Иностранный язык', '113', 'Сур В. В.'),
(5, '2017-11-11', '13:00-14:30; 14:40-16:10', 'Физика', '330', 'Беланов А. С.'),
(6, '2017-11-25', '13:00-14:30; 14:40-16:10', 'Информатика', '251', 'Карташов С. И.'),
(7, '2017-12-02', '10:40-12-10; 13:00-14:30', 'Методы и средства реализации информационных технологий', 'Ю. З.', 'Никольский А. Н.'),
(8, '2017-12-02', '14:40-16:10; 16:20-17:50', 'Программирование информационных систем', 'Ю. З.', 'Мерсов А. А.'),
(9, '2017-12-09', '9:00-10:30; 10:40-12:10', 'Математический анализ', '347', 'Ягудин Ш. С.'),
(10, '2017-12-16', '9:00-10:30; 10:40-12:10', 'Русский язык и культура речи', '381', 'Тарасова Е. Н.');
COMMIT;