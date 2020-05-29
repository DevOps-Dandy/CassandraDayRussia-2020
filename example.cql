
CREATE KEYSPACE a_kayspace
WITH REPLICATION = { 
   'class' : 'SimpleStrategy', 
      'replication_factor' : 1 

};

CREATE TABLE a_kayspace.a_table (
   a_int int, 
   a_str text, 
   a_bool boolean, 
   PRIMARY KEY (a_int, a_str));
