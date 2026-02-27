SELECT
    f.id_numfac,
	f.numfac,
	f.numdoc,
	f.cliente,
	f.numser,
	f.secuencia,
	f.comen1,
	f.comen2,
	f.comen3,
	f.subtotal,
	f.desc0,
	f.iva,
	f.total_iva ,
	f.total,
	f.codven,
	f.fecha_hora
FROM security_data.facturas f
ORDER BY f.emision DESC
LIMIT 100
