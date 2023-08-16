-- Analise superficial
SELECT
    codigocentrocusto,
    COUNT(*) as num_colaboradores
FROM
    colaboradores
WHERE
    is_ultimo_cargo = 'S'  and status = 'ATV'
GROUP BY
    codigocentrocusto;

-- Analise aprofundada lv 2
SELECT
    codigocentrocusto,
    descricaotipocargo,
    COUNT(*) as num_colaboradores
FROM
    colaboradores
WHERE
    is_ultimo_cargo = 'S' AND status = 'ATV'
GROUP BY
    codigocentrocusto, descricaotipocargo
ORDER BY
    codigocentrocusto, descricaotipocargo;

-- Analise aprofundada lv 3

SELECT
    c.codigocentrocusto,
    c.descricaotipocargo,
    c.razaosocial,
    COUNT(*) as num_colaboradores
FROM
    colaboradores c
WHERE
    c.is_ultimo_cargo = 'S' AND c.status = 'ATV'
GROUP BY
    c.codigocentrocusto, c.descricaotipocargo, c.razaosocial
ORDER BY
    c.codigocentrocusto, c.descricaotipocargo, c.razaosocial;