

create table institution
(
    id           SERIAL primary key,
    name         varchar(100) null,
    description  varchar(500) null,
    address      varchar(200) null,
    created_user varchar(100) null,
    created_at   TIMESTAMP      null,
    updated_user varchar(100) null,
    updated_at   TIMESTAMP     null,
    status       varchar(1)   null
);

INSERT INTO institution (id, name, description, address, created_user, created_at, updated_user, updated_at, status) VALUES (1, 'Platzi', 'Educacion on line', 'Colombia - Bogota', 'admin', '2023-01-26 18:24:48', null, null, 'A');
INSERT INTO institution (id, name, description, address, created_user, created_at, updated_user, updated_at, status) VALUES (2, 'Unemi', 'Educacion universitaria', 'Ecuador - Milagro', 'admin', '2023-01-26 18:25:27', null, null, 'A');

alter sequence institution_id_seq restart 3;

create table usuario
(
    id           SERIAL primary key,
    first_name   varchar(100) null,
    last_name    varchar(100) null,
    rut          varchar(100) null,
    birth_date   date         null,
    position     varchar(100) null,
    age          integer          null,
    created_user varchar(100) null,
    created_at   TIMESTAMP     null,
    updated_user varchar(100) null,
    updated_at   TIMESTAMP     null,
    status       varchar(1)   null
);

INSERT INTO usuario (id, first_name, last_name, rut, birth_date, position, age, created_user, created_at, updated_user, updated_at, status) VALUES (1, 'Luis', 'Torres', '1206260647', '1989-01-26', 'developer', 34, 'admin', '2023-01-26 18:19:58', null, null, 'A');
INSERT INTO usuario (id, first_name, last_name, rut, birth_date, position, age, created_user, created_at, updated_user, updated_at, status) VALUES (2, 'Pepe', 'Cabrera', '9876543210', '1987-08-10', 'ceo', 35, 'admin', '2023-01-26 18:20:50', null, null, 'A');
INSERT INTO usuario (id, first_name, last_name, rut, birth_date, position, age, created_user, created_at, updated_user, updated_at, status) VALUES (3, 'Guissela', 'Bermeo', '1234567890', '2000-01-26', 'tester', 13, 'admin', '2023-01-26 18:22:21', null, null, 'A');

create table proyect
(
    id            SERIAL primary key,
    name          varchar(100) null,
    description   varchar(500) null,
    start_date    date         null,
    end_date      date         null,
    created_user  varchar(100) null,
    created_at    TIMESTAMP     null,
    updated_user  varchar(100) null,
    updated_at    TIMESTAMP     null,
    status        varchar(1)   null,
    institutionid integer          null,
    usuarioid        integer          null,
    constraint proyect_institution_id_fk
        foreign key (institutionid) references institution (id),
    constraint proyect_user_id_fk
        foreign key (usuarioid) references usuario (id)
);

INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (1, 'Nuevo curso Python basico', 'Facilita el inicio en el desarrollo de software con python', '2023-01-01', '2023-01-31', 'admin', '2023-01-26 18:23:52', null, null, 'A', 1, 1);
INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (2, 'Curso intermedio de python', 'Permite que que el desarrollador use buenas practicas para el desarrollo apis ', '2023-02-01', '2023-02-28', 'admin', '2023-01-26 18:26:51', null, null, 'A', 1, 2);
INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (3, 'Curso de Computaci??n B??sica', 'Aprende c??mo sacar el m??ximo provecho de tu computadora.', '2023-03-01', '2023-03-31', 'admin', '2023-01-26 18:28:00', null, null, 'A', 1, 1);
INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (5, 'Curso Profesional de Git y GitHub', 'Deja de versionar tus proyectos usando tu propio sistema de control de versiones. Mejor usa Git, el sistema de control de versiones por excelencia que utiliza la industria tecnol??gica. Aprende a trabajar con git, conceptos b??sicos, clonar un repositorio y gestionar tus proyectos aloj??ndolos en tu repositorio local y en GitHub.', '2023-01-17', '2023-03-06', 'admin', '2023-01-26 18:57:22', null, null, 'A', 1, 3);
INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (6, 'Fundamentos de Ingenier??a de Software', 'Comienza tu proyecto aprendiendo las bases de la ingenier??a de software. En este curso podr??s entender c??mo funcionan las bases de la electr??nica, los diferentes sistemas operativos y las redes que te permiten usar Internet.', '2023-01-30', '2023-02-13', 'admin', '2023-01-26 18:58:07', null, null, 'A', 1, 3);
INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (7, 'Curso de Introducci??n al Pensamiento Computacional con Python', 'Comienza tu camino en el desarrollo de software con el lenguaje de programaci??n Python. Entiende la estructura de pensamiento necesaria para resolver problemas en programaci??n. Domina las estructuras de control para crear soluciones. Conoce las caracter??sticas de Python que te permiten reutilizar c??digo. Prueba tu c??digo e implementa correcciones y mejoras.', '2023-02-08', '2023-03-02', 'admin', '2023-01-26 18:58:48', null, null, 'A', 1, 2);
INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (8, 'Curso de Frontend Developer', 'Domina las bases de HTML y CSS. Conoce la anatom??a de un documento HTML, sus elementos y las propiedades de CSS. Maqueta las pantallas principales de tu p??gina web con responsive design. ??Conviertete en Frontend Developer con Platzi!', '2023-01-03', '2023-02-12', 'admin', '2023-01-26 18:59:41', null, null, 'A', 1, 1);
INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (9, 'Curso Pr??ctico de JavaScript', 'Aprender un lenguaje de programaci??n requiere de pr??ctica constante, con JavaScript puedes crear proyectos incre??bles que logren resolver problemas de la vida real por medio de aplicaciones web. En este curso aprender??s c??mo usar JavaScript para resolver problemas reales y pondr??s en pr??ctica todos tus conocimientos de JavaScript junto a tu profesor JuanDC.', '2023-01-15', '2023-03-08', 'admin', '2023-01-26 19:01:15', null, null, 'A', 1, 1);
INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (10, 'Curso de Asincronismo con JavaScript', 'Apropia los conceptos fundamentales de asincronismo con JavaScript, aplica sus diferentes estructuras y desarrolla soluciones as??ncronas. ??Ampl??a tus conocimientos de programaci??n creando una landing page!', '2023-01-04', '2023-02-05', 'admin', '2023-01-26 19:01:52', null, null, 'A', 1, 2);
INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (11, 'Curso Pr??ctico de React.js', '??Convierte tus dise??os en HTML y CSS a componentes reutilizables en React.js! Configura tu entorno de desarrollo con Webpack y Babel. Define los componentes, contenedores, rutas, react hooks de tu proyecto. Despliega tu proyecto a producci??n con Netlify. Convi??rtete en React Developer profesional con tu profesor Oscar Barajas.', '2023-01-24', '2023-04-05', 'admin', '2023-01-26 19:02:31', null, null, 'A', 1, 2);
INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (12, 'Curso Pr??ctico de Next.js', '??Aprende desarrollo FullStack con Next.js, el framework m??s importante de React.js! Descubre c??mo migrar proyectos de React.js y Webpack a Next.js.', '2023-01-02', '2023-02-07', 'admin', '2023-01-26 19:04:16', null, null, 'A', 2, 1);
INSERT INTO proyect (id, name, description, start_date, end_date, created_user, created_at, updated_user, updated_at, status, institutionid, usuarioid) VALUES (13, 'Curso de Prework: Configuraci??n de Entorno de Desarrollo en Linux', 'Instala y configura un sistema operativo Linux desde cero de diversas maneras. Agrega un editor de texto, terminal y diferentes herramientas para tener un entorno profesional de desarrollo.', '2023-01-16', '2023-03-07', 'admin', '2023-01-26 19:06:19', null, null, 'A', 2, 2);
