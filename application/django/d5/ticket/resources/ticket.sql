create table ticket_ticket
(
  id  integer not null
    constraint ticket_id
    primary key,
  key uuid not null
    constraint ticket_key
    unique,
  account_key uuid not null,
  status varchar(20),
  subject text
);