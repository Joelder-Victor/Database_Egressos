
CREATE TABLE turno(
    turno_id SERIAL,
    nome VARCHAR(255) NOT NULL,
    PRIMARY KEY (turno_id)
);
CREATE TABLE grau_academico(
    grau_academico_id SERIAL,
    nome VARCHAR(255),

    PRIMARY KEY (grau_academico_id)
    /*INDEX USING BTREE(nome)*/
);
CREATE TABLE centro(
    centro_id SERIAL,
    nome VARCHAR(255),
    
    PRIMARY KEY (centro_id)
    /*INDEX USING BTREE(nome)*/

);
CREATE TABLE campus(
    campus_id SERIAL,
    nome VARCHAR(255),
    
    PRIMARY KEY (campus_id)
    /*INDEX USING BTREE(nome)*/
);
CREATE TABLE situacao_curso(
    situacao_curso_id SERIAL,
    nome VARCHAR(255),

    PRIMARY KEY (situacao_curso_id)
);
CREATE TABLE nivel(
    nivel_id SERIAL,
    nome CHARACTER,

    PRIMARY KEY (nivel_id)
);
CREATE TABLE curso(
    curso_id SERIAL,
    nome VARCHAR(255),
    codigo_inep INTEGER,
    nivel_id INTEGER,
    situacao_curso_id INTEGER,
    centro_id INTEGER,
    campus_id INTEGER,
    grau_academico_id INTEGER,
    turno_id INTEGER,

    PRIMARY KEY (curso_id),
    /*INDEX USING BTREE (nome),*/

    FOREIGN KEY (nivel_id)
    REFERENCES nivel(nivel_id)
    ON DELETE CASCADE ON UPDATE CASCADE,

    FOREIGN KEY (situacao_curso_id)
    REFERENCES situacao_curso(situacao_curso_id)
    ON DELETE CASCADE ON UPDATE CASCADE,

    FOREIGN KEY(centro_id)
    REFERENCES centro(centro_id)
    ON DELETE CASCADE ON UPDATE CASCADE,

    FOREIGN KEY(campus_id)
    REFERENCES campus(campus_id)
    ON DELETE CASCADE ON UPDATE CASCADE,

    FOREIGN KEY(grau_academico_id)
    REFERENCES grau_academico(grau_academico_id)
    ON DELETE CASCADE ON UPDATE CASCADE,

    FOREIGN KEY(turno_id)
    REFERENCES turno(turno_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Sexo(
    sexo_id SERIAL,
    nome CHARACTER,

    PRIMARY KEY (sexo_id)
);
CREATE TABLE mun_residen(
    mun_residen_id SERIAL,
    nome VARCHAR(255),

    PRIMARY KEY(mun_residen_id)
);
CREATE TABLE egresso(
    cpf INTEGER ,
    ano_conclusao INTEGER,
    periodo_conclusao INTEGER,
    ano_ingresso INTEGER,
    periodo_ingresso INTEGER,
    data_nascimento DATE,
    cra INTEGER,
    sexo_id INTEGER,
    mun_residen_id INTEGER,
    curso_id INTEGER,

    FOREIGN KEY (sexo_id) 
    REFERENCES sexo(sexo_id)
    ON DELETE CASCADE ON UPDATE  CASCADE,

    FOREIGN KEY (mun_residen_id)
    REFERENCES mun_residen(mun_residen_id)
    ON DELETE CASCADE ON UPDATE CASCADE,

    FOREIGN KEY (curso_id)
    REFERENCES curso(curso_id)
    ON DELETE CASCADE ON UPDATE  CASCADE
);