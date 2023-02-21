-- Export of keyspace lauramolinos
CREATE KEYSPACE lauramolinos
WITH durable_writes = true
AND replication = {
	'class' : 'SimpleStrategy',
	'replication_factor' : 1
};

CREATE TABLE lauramolinos."Provincia_por_ProCod" (
	"Provincia_ProCod" text,
	"Provincia_JefesProvinciales" SET<text>,
	"Provincia_Nombre" text,
	PRIMARY KEY ("Provincia_ProCod")
) WITH bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Zona_por_ZonCod" (
	"Zona_ZonCod" text,
	"Zona_Municipios" SET<text>,
	"Zona_Nombre" text,
	PRIMARY KEY ("Zona_ZonCod")
) WITH bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Tabla6" (
	"Estacion_CodEst" text,
	"Linea_CodLin" text,
	"DistribucionDeRed_CodDis" text,
	"DistribucionDeRed_LongitudMaxima" float,
	"Estacion_Nombre" text,
	"Linea_Longitud" float,
	PRIMARY KEY ("Estacion_CodEst", "Linea_CodLin")
) WITH CLUSTERING ORDER BY ( "Linea_CodLin" ASC )
AND bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Tabla7" (
	"DistribucionDeRed_LongitudMaxima" float,
	"DistribucionDeRed_CodDis" text,
	"Productor_CodPro" text,
	"Estacion_CodEst" text,
	"Estacion_Nombre" text,
	"Productor_MaximaProduccion" float,
	"Productor_MediaProduccion" float,
	"Productor_Nombre" text,
	"Productor_OrigenEnergia" text,
	"Productor_Pais" text,
	PRIMARY KEY ("DistribucionDeRed_LongitudMaxima", "DistribucionDeRed_CodDis", "Productor_CodPro")
) WITH CLUSTERING ORDER BY ( "DistribucionDeRed_CodDis" ASC, "Productor_CodPro" ASC )
AND bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Productor_por_CodPro" (
	"Productor_CodPro" text,
	"Productor_MaximaProduccion" float,
	"Productor_MediaProduccion" float,
	"Productor_Nombre" text,
	"Productor_OrigenEnergia" text,
	"Productor_Pais" text,
	PRIMARY KEY ("Productor_CodPro")
) WITH bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Tabla8" (
	"Productor_Pais" text,
	"Productor_OrigenEnergia" text,
	"Productor_CodPro" text,
	"Productor_MaximaProduccion" float,
	"Productor_MediaProduccion" float,
	"Productor_Nombre" text,
	PRIMARY KEY (( "Productor_Pais", "Productor_OrigenEnergia" ), "Productor_CodPro")
) WITH CLUSTERING ORDER BY ( "Productor_CodPro" ASC )
AND bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."DistribucionDeRed_por_CodDis" (
	"DistribucionDeRed_CodDis" text,
	"DistribucionDeRed_LongitudMaxima" float,
	PRIMARY KEY ("DistribucionDeRed_CodDis")
) WITH bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Estacion_por_CodEst" (
	"Estacion_CodEst" text,
	"Estacion_Nombre" text,
	PRIMARY KEY ("Estacion_CodEst")
) WITH bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Tabla2" (
	"Zona_Nombre" text,
	"Zona_ZonCod" text,
	"Provincia_JefesProvinciales" SET<text>,
	"Provincia_Nombre" text,
	"Provincia_ProCod" text,
	"Zona_Municipios" SET<text>,
	PRIMARY KEY ("Zona_Nombre", "Zona_ZonCod")
) WITH CLUSTERING ORDER BY ( "Zona_ZonCod" ASC )
AND bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Tabla3" (
	"Estacion_CodEst" text,
	"Num_DistribucionDeRed" counter,
	PRIMARY KEY ("Estacion_CodEst")
) WITH bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Tabla4" (
	"Zona_Municipios" text,
	"Zona_ZonCod" text,
	"Zona_Municipios_set" SET<text>,
	"Zona_Nombre" text,
	PRIMARY KEY ("Zona_Municipios", "Zona_ZonCod")
) WITH CLUSTERING ORDER BY ( "Zona_ZonCod" ASC )
AND bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Tabla5" (
	"Distribuye_Fecha" date,
	"Subestacion_CodSub" text,
	"Zona_ZonCod" text,
	"Distribuye_Cantidad" float,
	"Subestacion_Capacidad" float,
	"Zona_Municipios" SET<text>,
	"Zona_Nombre" text,
	PRIMARY KEY ("Distribuye_Fecha", "Subestacion_CodSub", "Zona_ZonCod")
) WITH CLUSTERING ORDER BY ( "Subestacion_CodSub" ASC, "Zona_ZonCod" ASC )
AND bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Tabla1" (
	"Productor_Pais" text,
	"Productor_CodPro" text,
	"Productor_MaximaProduccion" float,
	"Productor_MediaProduccion" float,
	"Productor_Nombre" text,
	"Productor_OrigenEnergia" text,
	PRIMARY KEY ("Productor_Pais", "Productor_CodPro")
) WITH CLUSTERING ORDER BY ( "Productor_CodPro" ASC )
AND bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

CREATE TABLE lauramolinos."Subestacion_por_CodSub" (
	"Subestacion_CodSub" text,
	"Subestacion_Capacidad" float,
	PRIMARY KEY ("Subestacion_CodSub")
) WITH bloom_filter_fp_chance = 0.01
AND comment = ''
AND crc_check_chance = 1.0
AND dclocal_read_repair_chance = 0.1
AND default_time_to_live = 0
AND gc_grace_seconds = 864000
AND max_index_interval = 2048
AND memtable_flush_period_in_ms = 0
AND min_index_interval = 128
AND read_repair_chance = 0.0
AND speculative_retry = '99.0PERCENTILE'
AND caching = {
	'keys' : 'ALL',
	'rows_per_partition' : 'NONE'
}
AND compression = {
	'chunk_length_in_kb' : 64,
	'class' : 'LZ4Compressor',
	'enabled' : true
}
AND compaction = {
	'class' : 'SizeTieredCompactionStrategy',
	'max_threshold' : 32,
	'min_threshold' : 4
};

