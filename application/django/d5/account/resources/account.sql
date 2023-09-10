create table account
(
    id            integer not null
        constraint account_id
            primary key,
    key           integer not null
        constraint account_key
            unique,
    primary_email integer,
    password      integer,
    display_name  integer,
    last_login    timestamp
);