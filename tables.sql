CREATE TABLE Users (
  user_id SERIAL PRIMARY KEY NOT NULL,
  first_name VARCHAR(10),
  last_name VARCHAR(10),
  e_mail VARCHAR(20) NOT NULL,
  phone_number VARCHAR(10),
  password VARCHAR(10) NOT NULL,
  user_name VARCHAR(10) NOT NULL
);

CREATE TABLE Chat (
  chat_id SERIAL PRIMARY KEY NOT NULL,
  chat_name VARCHAR(10) NOT NULL,
  manager INTEGER REFERENCES Users(user_id) NOT NULL
);

CREATE TABLE Message (
  message_id SERIAL PRIMARY KEY NOT NULL,
  sender INTEGER REFERENCES Users(user_id) NOT NULL,
  content VARCHAR(200) NOT NULL,
  reply_id INTEGER,
  time_stamp TIMESTAMP DEFAULT NOW() NOT NULL,
  FOREIGN KEY (reply_id) REFERENCES Message(message_id)
);

CREATE TABLE Member (
	user_id INTEGER REFERENCES Users(user_id) NOT NULL,
	chat_id INTEGER REFERENCES Chat(chat_id) NOT NULL,
	PRIMARY KEY (user_id, chat_id)
);

CREATE TABLE Contact (
	user_id INTEGER REFERENCES Users(user_id) NOT NULL,
	contact_id INTEGER REFERENCES Users(user_id) NOT NULL,
	PRIMARY KEY (user_id, contact_id)
);

CREATE TABLE Like_Dislike (
	user_id INTEGER REFERENCES Users(user_id) NOT NULL,
	message_id INTEGER REFERENCES Message (message_id) NOT NULL,
	like_dislike BOOLEAN NOT NULL,
	PRIMARY KEY (user_id, message_id)
);

CREATE TABLE Reply (
	user_id INTEGER REFERENCES Users(user_id) NOT NULL,
	message_id INTEGER REFERENCES Message(message_id) NOT NULL,
	PRIMARY KEY (user_id, message_id)
);

CREATE TABLE Contains (
	chat_id INTEGER REFERENCES Chat(chat_id) NOT NULL,
	message_id INTEGER REFERENCES Message (message_id) NOT NULL,
	PRIMARY KEY (chat_id, message_id)
);