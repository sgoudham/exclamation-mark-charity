PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS TeamTournament;
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Tournament;
DROP TABLE IF EXISTS University;
DROP TABLE IF EXISTS Player;

CREATE TABLE IF NOT EXISTS University
(
    pk_university_id INTEGER PRIMARY KEY,
    name             TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Team
(
    pk_team_id               INTEGER PRIMARY KEY,
    name                     TEXT UNIQUE NOT NULL,
    discord_category_id      TEXT,
    discord_text_channel_id  TEXT,
    discord_voice_channel_id TEXT,
    fk_tournament_id         INTEGER,
    fk_university_id         INTEGER,
    FOREIGN KEY (fk_university_id)
        REFERENCES University (pk_university_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (fk_tournament_id)
        REFERENCES Tournament (pk_tournament_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Player
(
    pk_player_id     INTEGER PRIMARY KEY,
    battlenet_id     TEXT UNIQUE NOT NULL,
    discord_tag      TEXT,
    skill_rating     TEXT,
    roles            TEXT CHECK (roles in ('TANK', 'DPS', 'SUPPORT', 'FLEX')),
    preferred_hero   TEXT,
    fk_university_id INTEGER,
    fk_team_id       INTEGER,
    FOREIGN KEY (fk_university_id)
        REFERENCES University (pk_university_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL,
    FOREIGN KEY (fk_team_id)
        REFERENCES Team (pk_team_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Tournament
(
    pk_tournament_id INTEGER PRIMARY KEY,
    name             TEXT UNIQUE NOT NULL,
    money_raised     INTEGER DEFAULT 0,
    mvp              INTEGER DEFAULT NULL,
    FOREIGN KEY (mvp)
        REFERENCES Player (pk_player_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS TeamTournament
(
    pk_fk_tournament_id INTEGER NOT NULL,
    pk_fk_team_id       INTEGER NOT NULL,
    tournament_status   TEXT CHECK (tournament_status in ('IN', 'OUT')),
    PRIMARY KEY (pk_fk_tournament_id, pk_fk_team_id),
    FOREIGN KEY (pk_fk_tournament_id)
        REFERENCES Tournament (pk_tournament_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (pk_fk_team_id)
        REFERENCES Team (pk_team_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);