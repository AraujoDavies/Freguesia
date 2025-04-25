SELECT_RESULTADO_MENSAL = """
SELECT 
* 
FROM (SELECT 
DATE(concat(YEAR(data_partida), '-', MONTH(data_partida), '-1')) mensal,  
SUM(IF(fregues="visitante" and resultado IS NOT NULL AND odd_mandante<=@odd_max AND odd_mandante>=@odd_min, 1, 0)) qt_entradas_mandantes,
SUM(IF(fregues="visitante" and resultado="green" AND odd_mandante<=@odd_max AND odd_mandante>=@odd_min, 1, 0)) qt_green_mandantes,
SUM(IF(fregues="visitante" and resultado="red" AND odd_mandante<=@odd_max AND odd_mandante>=@odd_min, 1, 0)) qt_red_mandantes,
SUM(IF(fregues="visitante" AND odd_mandante<=@odd_max AND odd_mandante>=@odd_min and resultado IS NOT NULL, IF(resultado="green", odd_mandante - 1, -1), 0)) pl_mandantes,

SUM(IF(fregues="mandante" and resultado IS NOT NULL AND odd_visitante<=@odd_max AND odd_visitante>=@odd_min, 1, 0)) qt_entradas_visitantes,
SUM(IF(fregues="mandante" and resultado="green" AND odd_visitante<=@odd_max AND odd_visitante>=@odd_min, 1, 0)) qt_green_visitantes,
SUM(IF(fregues="mandante" and resultado="red" AND odd_visitante<=@odd_max AND odd_visitante>=@odd_min, 1, 0)) qt_red_visitantes,
SUM(IF(fregues="mandante" AND odd_visitante<=@odd_max AND odd_visitante>=@odd_min and resultado IS NOT NULL, IF(resultado="green", odd_visitante - 1, -1), 0)) pl_visitantes,

SUM(IF(fregues="visitante" AND odd_mandante<=@odd_max AND odd_mandante>=@odd_min and resultado IS NOT NULL, IF(resultado="green", odd_mandante - 1, -1), 0) + IF(fregues="mandante" AND odd_visitante<=@odd_max AND odd_visitante>=@odd_min and resultado IS NOT NULL, IF(resultado="green", odd_visitante - 1, -1), 0) ) pl_total
FROM academia.padrao_freguesia 
GROUP BY 
DATE(concat(YEAR(data_partida), '-', MONTH(data_partida), '-1'))
ORDER BY mensal
) mensal WHERE mensal >= DATE_SUB(CURDATE(), INTERVAL 13 MONTH);
"""

# > OBS: Troque o "DATE(concat(YEAR(data_partida), '-', MONTH(data_partida), '-1'))" por "campeonato" e terá o resultado por campeonato