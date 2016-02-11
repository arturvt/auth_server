drop table if exists auth_keys;
create table auth_keys (
  id integer primary key autoincrement,
  reader_key text unique not null,
  machine_id text,
  created_date text not null,
  authenticated_date text
);
