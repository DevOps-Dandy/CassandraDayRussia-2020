
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

use a_kayspace;

CREATE TRIGGER kafka_trigger ON a_table USING 'io.smartcat.cassandra.trigger.KafkaTrigger';

INSERT INTO a_table ( a_int , a_str , a_bool ) VALUES ( 1, 'a', true );
SELECT count(*) FROM a_kayspace.a_table;

