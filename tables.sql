--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

-- Started on 2018-04-29 20:09:32 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE db_project;
--
-- TOC entry 2214 (class 1262 OID 16385)
-- Name: db_project; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE db_project WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE db_project OWNER TO postgres;

\connect db_project

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12395)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2217 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 184 (class 1259 OID 16402)
-- Name: chat; Type: TABLE; Schema: public; Owner: siramul94
--

CREATE TABLE public.chat (
    chat_id integer NOT NULL,
    chat_name character varying(10) NOT NULL,
    manager integer NOT NULL
);


ALTER TABLE public.chat OWNER TO siramul94;

--
-- TOC entry 183 (class 1259 OID 16400)
-- Name: chat_chat_id_seq; Type: SEQUENCE; Schema: public; Owner: siramul94
--

CREATE SEQUENCE public.chat_chat_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chat_chat_id_seq OWNER TO siramul94;

--
-- TOC entry 2218 (class 0 OID 0)
-- Dependencies: 183
-- Name: chat_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: siramul94
--

ALTER SEQUENCE public.chat_chat_id_seq OWNED BY public.chat.chat_id;


--
-- TOC entry 188 (class 1259 OID 16447)
-- Name: contact; Type: TABLE; Schema: public; Owner: siramul94
--

CREATE TABLE public.contact (
    user_id integer NOT NULL,
    contact_id integer NOT NULL
);


ALTER TABLE public.contact OWNER TO siramul94;

--
-- TOC entry 191 (class 1259 OID 16492)
-- Name: contains; Type: TABLE; Schema: public; Owner: siramul94
--

CREATE TABLE public.contains (
    chat_id integer NOT NULL,
    message_id integer NOT NULL
);


ALTER TABLE public.contains OWNER TO siramul94;

--
-- TOC entry 189 (class 1259 OID 16462)
-- Name: like_dislike; Type: TABLE; Schema: public; Owner: siramul94
--

CREATE TABLE public.like_dislike (
    user_id integer NOT NULL,
    message_id integer NOT NULL,
    like_dislike boolean NOT NULL
);


ALTER TABLE public.like_dislike OWNER TO siramul94;

--
-- TOC entry 187 (class 1259 OID 16432)
-- Name: member; Type: TABLE; Schema: public; Owner: siramul94
--

CREATE TABLE public.member (
    user_id integer NOT NULL,
    chat_id integer NOT NULL
);


ALTER TABLE public.member OWNER TO siramul94;

--
-- TOC entry 186 (class 1259 OID 16415)
-- Name: message; Type: TABLE; Schema: public; Owner: siramul94
--

CREATE TABLE public.message (
    message_id integer NOT NULL,
    sender integer NOT NULL,
    content character varying(200) NOT NULL,
    reply_id integer,
    time_stamp timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.message OWNER TO siramul94;

--
-- TOC entry 185 (class 1259 OID 16413)
-- Name: message_message_id_seq; Type: SEQUENCE; Schema: public; Owner: siramul94
--

CREATE SEQUENCE public.message_message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.message_message_id_seq OWNER TO siramul94;

--
-- TOC entry 2219 (class 0 OID 0)
-- Dependencies: 185
-- Name: message_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: siramul94
--

ALTER SEQUENCE public.message_message_id_seq OWNED BY public.message.message_id;


--
-- TOC entry 190 (class 1259 OID 16477)
-- Name: reply; Type: TABLE; Schema: public; Owner: siramul94
--

CREATE TABLE public.reply (
    user_id integer NOT NULL,
    message_id integer NOT NULL
);


ALTER TABLE public.reply OWNER TO siramul94;

--
-- TOC entry 182 (class 1259 OID 16392)
-- Name: users; Type: TABLE; Schema: public; Owner: siramul94
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    first_name character varying(20),
    last_name character varying(20),
    e_mail character varying(254) NOT NULL,
    phone character varying(11),
    password character varying(20) NOT NULL,
    user_name character varying(10) NOT NULL
);


ALTER TABLE public.users OWNER TO siramul94;

--
-- TOC entry 181 (class 1259 OID 16390)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: siramul94
--

CREATE SEQUENCE public.users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO siramul94;

--
-- TOC entry 2220 (class 0 OID 0)
-- Dependencies: 181
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: siramul94
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- TOC entry 2052 (class 2604 OID 16405)
-- Name: chat_id; Type: DEFAULT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.chat ALTER COLUMN chat_id SET DEFAULT nextval('public.chat_chat_id_seq'::regclass);


--
-- TOC entry 2053 (class 2604 OID 16418)
-- Name: message_id; Type: DEFAULT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.message ALTER COLUMN message_id SET DEFAULT nextval('public.message_message_id_seq'::regclass);


--
-- TOC entry 2051 (class 2604 OID 16395)
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- TOC entry 2201 (class 0 OID 16402)
-- Dependencies: 184
-- Data for Name: chat; Type: TABLE DATA; Schema: public; Owner: siramul94
--

INSERT INTO public.chat (chat_id, chat_name, manager) VALUES (2, 'sis4ever', 1);
INSERT INTO public.chat (chat_id, chat_name, manager) VALUES (4, 'my_baby', 2);
INSERT INTO public.chat (chat_id, chat_name, manager) VALUES (6, 'cu~is', 3);


--
-- TOC entry 2221 (class 0 OID 0)
-- Dependencies: 183
-- Name: chat_chat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: siramul94
--

SELECT pg_catalog.setval('public.chat_chat_id_seq', 6, true);


--
-- TOC entry 2205 (class 0 OID 16447)
-- Dependencies: 188
-- Data for Name: contact; Type: TABLE DATA; Schema: public; Owner: siramul94
--

INSERT INTO public.contact (user_id, contact_id) VALUES (1, 2);
INSERT INTO public.contact (user_id, contact_id) VALUES (1, 3);


--
-- TOC entry 2208 (class 0 OID 16492)
-- Dependencies: 191
-- Data for Name: contains; Type: TABLE DATA; Schema: public; Owner: siramul94
--



--
-- TOC entry 2206 (class 0 OID 16462)
-- Dependencies: 189
-- Data for Name: like_dislike; Type: TABLE DATA; Schema: public; Owner: siramul94
--

INSERT INTO public.like_dislike (user_id, message_id, like_dislike) VALUES (1, 2, true);
INSERT INTO public.like_dislike (user_id, message_id, like_dislike) VALUES (1, 1, true);
INSERT INTO public.like_dislike (user_id, message_id, like_dislike) VALUES (2, 1, false);


--
-- TOC entry 2204 (class 0 OID 16432)
-- Dependencies: 187
-- Data for Name: member; Type: TABLE DATA; Schema: public; Owner: siramul94
--



--
-- TOC entry 2203 (class 0 OID 16415)
-- Dependencies: 186
-- Data for Name: message; Type: TABLE DATA; Schema: public; Owner: siramul94
--

INSERT INTO public.message (message_id, sender, content, reply_id, time_stamp) VALUES (1, 1, 'Hello!', NULL, '2018-04-24 00:17:54.596284');
INSERT INTO public.message (message_id, sender, content, reply_id, time_stamp) VALUES (2, 2, 'Wep', NULL, '2018-04-29 11:11:49.600586');
INSERT INTO public.message (message_id, sender, content, reply_id, time_stamp) VALUES (3, 1, 'Que es la que hay?', NULL, '2018-04-29 11:39:25.928777');
INSERT INTO public.message (message_id, sender, content, reply_id, time_stamp) VALUES (4, 2, 'Na', NULL, '2018-04-29 12:31:28.814782');


--
-- TOC entry 2222 (class 0 OID 0)
-- Dependencies: 185
-- Name: message_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: siramul94
--

SELECT pg_catalog.setval('public.message_message_id_seq', 4, true);


--
-- TOC entry 2207 (class 0 OID 16477)
-- Dependencies: 190
-- Data for Name: reply; Type: TABLE DATA; Schema: public; Owner: siramul94
--



--
-- TOC entry 2199 (class 0 OID 16392)
-- Dependencies: 182
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: siramul94
--

INSERT INTO public.users (user_id, first_name, last_name, e_mail, phone, password, user_name) VALUES (2, 'Dan', 'Rosa De Jesus', 'dan.rosa@upr.edu', '17874641523', 'chicodelarosa01', 'dancito');
INSERT INTO public.users (user_id, first_name, last_name, e_mail, phone, password, user_name) VALUES (3, 'Yacenia', 'Rios Melendez', 'yacenia.rios@upr.edu', '17872010569', 'y@c3n!@', 'angie');
INSERT INTO public.users (user_id, first_name, last_name, e_mail, phone, password, user_name) VALUES (1, 'Lumaris', 'Rios Melendez', 'lumaris.rios@upr.edu', '17873624204', 'NotCool01', 'siramul');


--
-- TOC entry 2223 (class 0 OID 0)
-- Dependencies: 181
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: siramul94
--

SELECT pg_catalog.setval('public.users_user_id_seq', 3, true);


--
-- TOC entry 2058 (class 2606 OID 16407)
-- Name: chat_pkey; Type: CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.chat
    ADD CONSTRAINT chat_pkey PRIMARY KEY (chat_id);


--
-- TOC entry 2064 (class 2606 OID 16451)
-- Name: contact_pkey; Type: CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.contact
    ADD CONSTRAINT contact_pkey PRIMARY KEY (user_id, contact_id);


--
-- TOC entry 2070 (class 2606 OID 16496)
-- Name: contains_pkey; Type: CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.contains
    ADD CONSTRAINT contains_pkey PRIMARY KEY (chat_id, message_id);


--
-- TOC entry 2066 (class 2606 OID 16466)
-- Name: like_dislike_pkey; Type: CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.like_dislike
    ADD CONSTRAINT like_dislike_pkey PRIMARY KEY (user_id, message_id);


--
-- TOC entry 2062 (class 2606 OID 16436)
-- Name: member_pkey; Type: CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_pkey PRIMARY KEY (user_id, chat_id);


--
-- TOC entry 2060 (class 2606 OID 16421)
-- Name: message_pkey; Type: CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.message
    ADD CONSTRAINT message_pkey PRIMARY KEY (message_id);


--
-- TOC entry 2068 (class 2606 OID 16481)
-- Name: reply_pkey; Type: CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.reply
    ADD CONSTRAINT reply_pkey PRIMARY KEY (user_id, message_id);


--
-- TOC entry 2056 (class 2606 OID 16397)
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- TOC entry 2071 (class 2606 OID 16408)
-- Name: chat_manager_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.chat
    ADD CONSTRAINT chat_manager_fkey FOREIGN KEY (manager) REFERENCES public.users(user_id);


--
-- TOC entry 2077 (class 2606 OID 16457)
-- Name: contact_contact_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.contact
    ADD CONSTRAINT contact_contact_id_fkey FOREIGN KEY (contact_id) REFERENCES public.users(user_id);


--
-- TOC entry 2076 (class 2606 OID 16452)
-- Name: contact_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.contact
    ADD CONSTRAINT contact_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- TOC entry 2082 (class 2606 OID 16497)
-- Name: contains_chat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.contains
    ADD CONSTRAINT contains_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES public.chat(chat_id);


--
-- TOC entry 2083 (class 2606 OID 16502)
-- Name: contains_message_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.contains
    ADD CONSTRAINT contains_message_id_fkey FOREIGN KEY (message_id) REFERENCES public.message(message_id);


--
-- TOC entry 2079 (class 2606 OID 16472)
-- Name: like_dislike_message_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.like_dislike
    ADD CONSTRAINT like_dislike_message_id_fkey FOREIGN KEY (message_id) REFERENCES public.message(message_id);


--
-- TOC entry 2078 (class 2606 OID 16467)
-- Name: like_dislike_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.like_dislike
    ADD CONSTRAINT like_dislike_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- TOC entry 2075 (class 2606 OID 16442)
-- Name: member_chat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES public.chat(chat_id);


--
-- TOC entry 2074 (class 2606 OID 16437)
-- Name: member_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- TOC entry 2073 (class 2606 OID 16427)
-- Name: message_reply_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.message
    ADD CONSTRAINT message_reply_id_fkey FOREIGN KEY (reply_id) REFERENCES public.message(message_id);


--
-- TOC entry 2072 (class 2606 OID 16422)
-- Name: message_sender_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.message
    ADD CONSTRAINT message_sender_fkey FOREIGN KEY (sender) REFERENCES public.users(user_id);


--
-- TOC entry 2081 (class 2606 OID 16487)
-- Name: reply_message_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.reply
    ADD CONSTRAINT reply_message_id_fkey FOREIGN KEY (message_id) REFERENCES public.message(message_id);


--
-- TOC entry 2080 (class 2606 OID 16482)
-- Name: reply_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: siramul94
--

ALTER TABLE ONLY public.reply
    ADD CONSTRAINT reply_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- TOC entry 2216 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2018-04-29 20:09:32 AST

--
-- PostgreSQL database dump complete
--

