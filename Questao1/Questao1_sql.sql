SELECT
    G1.codigocentrocusto,
    G1.nome,
    G1.descricaotipocargo,
    G1.gestornome as gestor1,
    G2.gestornome as gestor2,
    G3.gestornome as gestor3,
    G4.gestornome as gestor4,
    G5.gestornome as gestor5
FROM colaboradores G1
JOIN colaboradores G2 ON G1.gestornome = G2.nome AND G2.is_ultimo_cargo = 'S' AND G2.status ='ATV'
JOIN colaboradores G3 ON G2.gestornome = G3.nome AND G3.is_ultimo_cargo = 'S' AND G3.status ='ATV'
JOIN colaboradores G4 ON G3.gestornome = G4.nome AND G4.is_ultimo_cargo = 'S' AND G4.status ='ATV'
JOIN colaboradores G5 ON G4.gestornome = G5.nome AND G5.is_ultimo_cargo = 'S' AND G5.status ='ATV'
WHERE G1.is_ultimo_cargo = 'S' and G1.status ='ATV'
-- and G1.codigocentrocusto like '91059';