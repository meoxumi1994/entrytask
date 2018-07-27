CREATE DATABASE event_sharing_db;
USE event_sharing_db;

CREATE TABLE user_tab (
	id int NOT NULL AUTO_INCREMENT,
	user_name varchar(255),
    password varchar(255),
    address varchar(255),
    create_time datetime,
    full_name varchar(255),
    first_name varchar(255),
    last_name varchar(255),
    is_active boolean,
    user_type varchar(255),
    avatar varchar(255),
	create_by varchar(255),
    PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE event_tab (
	id int NOT NULL AUTO_INCREMENT,
    create_by int NOT NULL,
	create_time datetime,
    event_time datetime,
    location varchar(255),
    title varchar(255),
    description VARCHAR(2048),
    PRIMARY KEY (id),
    FOREIGN KEY (create_by) REFERENCES user_tab(id)
) ENGINE=InnoDB;
CREATE INDEX idx_create_by ON event_tab (create_by);

CREATE TABLE participants_tab (
	id int NOT NULL AUTO_INCREMENT,
	user_id int NOT NULL,
    event_id int NOT NULL,
    create_time datetime,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES user_tab(id),
    FOREIGN KEY (event_id) REFERENCES event_tab(id)
) ENGINE=InnoDB;
CREATE INDEX idx_event_id_create_time ON participants_tab (event_id, create_time);
CREATE INDEX idx_user_id_create_time ON participants_tab (user_id, create_time);

CREATE TABLE comment_tab (
	id int NOT NULL AUTO_INCREMENT,
    create_time datetime,
	user_id int NOT NULL,
    event_id int NOT NULL,
    content varchar(512),
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES user_tab(id),
    FOREIGN KEY (event_id) REFERENCES event_tab(id)
) ENGINE=InnoDB;
CREATE INDEX idx_event_id_create_time ON comment_tab (event_id, create_time);
CREATE INDEX idx_user_id_create_time ON comment_tab (user_id, create_time);

CREATE TABLE like_tab (
	id int NOT NULL AUTO_INCREMENT,
    create_time datetime,
	user_id int NOT NULL,
    event_id int NOT NULL,
    type varchar(255),
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES user_tab(id),
    FOREIGN KEY (event_id) REFERENCES event_tab(id)
) ENGINE=InnoDB;
CREATE INDEX idx_event_id_create_time ON like_tab (event_id, create_time);
CREATE INDEX idx_user_id_create_time ON like_tab (user_id, create_time);

CREATE TABLE category_tab (
	id int NOT NULL AUTO_INCREMENT,
    category_name varchar(255),
    create_time datetime,
    description varchar(255),
    category_photo varchar(255),
    PRIMARY KEY (id)
) ENGINE=InnoDB;
CREATE INDEX idx_category_name ON category_tab(category_name);

CREATE TABLE event_category_tab (
	id int NOT NULL AUTO_INCREMENT,
    event_id int NOT NULL,
    category_id int NOT NULL,
    create_time datetime,
    PRIMARY KEY (id),
    FOREIGN KEY (event_id) REFERENCES event_tab(id),
    FOREIGN KEY (category_id) REFERENCES category_tab(id)
) ENGINE=InnoDB;
CREATE INDEX idx_category_id_event_id ON event_category_tab(category_id, event_id);

CREATE TABLE tag_tab (
	id int NOT NULL AUTO_INCREMENT,
    tag_name varchar(255),
    create_time datetime,
    PRIMARY KEY (id)
) ENGINE=InnoDB;
CREATE INDEX idx_tag_name ON tag_tab(tag_name);

CREATE TABLE event_tag_tab (
	id int NOT NULL AUTO_INCREMENT,
    event_id int NOT NULL,
    tag_id int NOT NULL,
    create_by int NOT NULL,
    create_time datetime,
    PRIMARY KEY (id),
    FOREIGN KEY (event_id) REFERENCES event_tab(id),
    FOREIGN KEY (tag_id) REFERENCES tag_tab(id)
) ENGINE=InnoDB;
CREATE INDEX idx_tag_id_event_id ON event_tag_tab(tag_id, event_id)

