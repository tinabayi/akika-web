--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO bayizere;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO bayizere;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO bayizere;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO bayizere;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO bayizere;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO bayizere;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO bayizere;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO bayizere;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO bayizere;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO bayizere;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO bayizere;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO bayizere;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO bayizere;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO bayizere;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO bayizere;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO bayizere;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO bayizere;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO bayizere;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO bayizere;

--
-- Name: hive_academic; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.hive_academic (
    id integer NOT NULL,
    academic_name character varying(60) NOT NULL,
    academic_location character varying(60) NOT NULL,
    academic_email character varying(254) NOT NULL
);


ALTER TABLE public.hive_academic OWNER TO bayizere;

--
-- Name: hive_academic_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.hive_academic_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hive_academic_id_seq OWNER TO bayizere;

--
-- Name: hive_academic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.hive_academic_id_seq OWNED BY public.hive_academic.id;


--
-- Name: hive_business; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.hive_business (
    id integer NOT NULL,
    business_founder character varying(60) NOT NULL,
    business_name character varying(60) NOT NULL,
    business_location character varying(30) NOT NULL,
    business_email character varying(254) NOT NULL
);


ALTER TABLE public.hive_business OWNER TO bayizere;

--
-- Name: hive_business_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.hive_business_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hive_business_id_seq OWNER TO bayizere;

--
-- Name: hive_business_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.hive_business_id_seq OWNED BY public.hive_business.id;


--
-- Name: hive_enterprise; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.hive_enterprise (
    id integer NOT NULL,
    enterprise_founder character varying(60) NOT NULL,
    enterprise_name character varying(60) NOT NULL,
    enterprise_location character varying(30) NOT NULL,
    entrprise_email character varying(254) NOT NULL
);


ALTER TABLE public.hive_enterprise OWNER TO bayizere;

--
-- Name: hive_enterprise_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.hive_enterprise_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hive_enterprise_id_seq OWNER TO bayizere;

--
-- Name: hive_enterprise_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.hive_enterprise_id_seq OWNED BY public.hive_enterprise.id;


--
-- Name: hive_freelancer; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.hive_freelancer (
    id integer NOT NULL,
    freelancer_names character varying(60) NOT NULL,
    project_name character varying(60) NOT NULL,
    freelancer_email character varying(254) NOT NULL
);


ALTER TABLE public.hive_freelancer OWNER TO bayizere;

--
-- Name: hive_freelancer_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.hive_freelancer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hive_freelancer_id_seq OWNER TO bayizere;

--
-- Name: hive_freelancer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.hive_freelancer_id_seq OWNED BY public.hive_freelancer.id;


--
-- Name: hive_government; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.hive_government (
    id integer NOT NULL,
    institution_name character varying(60) NOT NULL,
    institution_location character varying(60) NOT NULL,
    institution_adress integer NOT NULL
);


ALTER TABLE public.hive_government OWNER TO bayizere;

--
-- Name: hive_government_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.hive_government_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hive_government_id_seq OWNER TO bayizere;

--
-- Name: hive_government_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.hive_government_id_seq OWNED BY public.hive_government.id;


--
-- Name: hive_image; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.hive_image (
    id integer NOT NULL,
    images character varying(100) NOT NULL,
    title character varying(30) NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.hive_image OWNER TO bayizere;

--
-- Name: hive_image_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.hive_image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hive_image_id_seq OWNER TO bayizere;

--
-- Name: hive_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.hive_image_id_seq OWNED BY public.hive_image.id;


--
-- Name: hive_newsletterrecipients; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.hive_newsletterrecipients (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    email character varying(254) NOT NULL
);


ALTER TABLE public.hive_newsletterrecipients OWNER TO bayizere;

--
-- Name: hive_newsletterrecipients_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.hive_newsletterrecipients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hive_newsletterrecipients_id_seq OWNER TO bayizere;

--
-- Name: hive_newsletterrecipients_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.hive_newsletterrecipients_id_seq OWNED BY public.hive_newsletterrecipients.id;


--
-- Name: hive_student; Type: TABLE; Schema: public; Owner: bayizere
--

CREATE TABLE public.hive_student (
    id integer NOT NULL,
    first_name character varying(60) NOT NULL,
    last_name character varying(60) NOT NULL,
    education_level character varying(120) NOT NULL,
    student_email character varying(254) NOT NULL
);


ALTER TABLE public.hive_student OWNER TO bayizere;

--
-- Name: hive_student_id_seq; Type: SEQUENCE; Schema: public; Owner: bayizere
--

CREATE SEQUENCE public.hive_student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hive_student_id_seq OWNER TO bayizere;

--
-- Name: hive_student_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bayizere
--

ALTER SEQUENCE public.hive_student_id_seq OWNED BY public.hive_student.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: hive_academic id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_academic ALTER COLUMN id SET DEFAULT nextval('public.hive_academic_id_seq'::regclass);


--
-- Name: hive_business id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_business ALTER COLUMN id SET DEFAULT nextval('public.hive_business_id_seq'::regclass);


--
-- Name: hive_enterprise id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_enterprise ALTER COLUMN id SET DEFAULT nextval('public.hive_enterprise_id_seq'::regclass);


--
-- Name: hive_freelancer id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_freelancer ALTER COLUMN id SET DEFAULT nextval('public.hive_freelancer_id_seq'::regclass);


--
-- Name: hive_government id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_government ALTER COLUMN id SET DEFAULT nextval('public.hive_government_id_seq'::regclass);


--
-- Name: hive_image id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_image ALTER COLUMN id SET DEFAULT nextval('public.hive_image_id_seq'::regclass);


--
-- Name: hive_newsletterrecipients id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_newsletterrecipients ALTER COLUMN id SET DEFAULT nextval('public.hive_newsletterrecipients_id_seq'::regclass);


--
-- Name: hive_student id; Type: DEFAULT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_student ALTER COLUMN id SET DEFAULT nextval('public.hive_student_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add academic	8	add_academic
20	Can change academic	8	change_academic
21	Can delete academic	8	delete_academic
22	Can add business	9	add_business
23	Can change business	9	change_business
24	Can delete business	9	delete_business
25	Can add enterprise	10	add_enterprise
26	Can change enterprise	10	change_enterprise
27	Can delete enterprise	10	delete_enterprise
28	Can add freelancer	11	add_freelancer
29	Can change freelancer	11	change_freelancer
30	Can delete freelancer	11	delete_freelancer
31	Can add government	12	add_government
32	Can change government	12	change_government
33	Can delete government	12	delete_government
34	Can add image	13	add_image
35	Can change image	13	change_image
36	Can delete image	13	delete_image
37	Can add student	14	add_student
38	Can change student	14	change_student
39	Can delete student	14	delete_student
40	Can add news letter recipients	15	add_newsletterrecipients
41	Can change news letter recipients	15	change_newsletterrecipients
42	Can delete news letter recipients	15	delete_newsletterrecipients
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$36000$yMMtPyUVz3E4$ehb9Je3woLjSe7HGzzqqsElYRxc+A7ZW/VJJ/MIwfGM=	\N	t	bayizere			bayizerechristine4@gmail.com	t	t	2019-10-24 16:45:46.154546+02
4	pbkdf2_sha256$36000$FXXBVggpFpwl$TTT0GMGwjXxJAoqwnx3tPEndc/4Vd/otjLfKPz0kXCA=	2019-10-28 17:35:54.155566+02	f	chris			bayizerechristine4@gmail.com	f	t	2019-10-28 17:35:53.925175+02
5	pbkdf2_sha256$36000$W1t9Z9tKEVtf$WCEW1biGTjSMvKly+a0jGH9k1oQ+ADTOvOODCei2qqY=	2019-10-28 17:49:05.384758+02	f	kiki			kiki@gmail.com	f	t	2019-10-28 17:49:05.217512+02
3	pbkdf2_sha256$36000$kD5gUKyYK8FJ$S4k/RZYiiC7dJOk0XBVCVmtoChmKh8+RDnqr2ik+y+0=	2019-10-29 08:22:53.851251+02	f	alice			umulisaa0@gmail.com	f	t	2019-10-28 17:14:09.728006+02
6	pbkdf2_sha256$36000$km1rmI9puvag$+OAqQ6EzdCs1IkqOrrakWoTTDHEqrZ/bLcW6U6o47BQ=	2019-10-29 08:31:06.219891+02	f	mama			claire@gmail.com	f	t	2019-10-29 08:31:06.040828+02
7	pbkdf2_sha256$36000$awMdeevGKhDC$9xchzWIyMfUrPQjNPaZd721G86Q7o9hKggREfXROVG0=	2019-10-29 08:33:56.646491+02	f	kaka			kiki@gmail.com	f	t	2019-10-29 08:33:56.504465+02
2	pbkdf2_sha256$36000$ogCyt9ZjMycy$h89oAW/EjYrSGrH7Kfd46sImztCRmSBSmhXuxVuBbx8=	2019-10-30 14:03:24.782468+02	t	christine			bayizerechristine4@gmail.com	t	t	2019-10-24 16:50:48.288422+02
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2019-10-29 17:30:46.008003+02	5	Student object	1	[{"added": {}}]	14	2
2	2019-10-29 17:39:19.629108+02	6	Student object	1	[{"added": {}}]	14	2
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	hive	product
8	hive	academic
9	hive	business
10	hive	enterprise
11	hive	freelancer
12	hive	government
13	hive	image
14	hive	student
15	hive	newsletterrecipients
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-10-24 15:14:06.29725+02
2	auth	0001_initial	2019-10-24 15:14:07.142451+02
3	admin	0001_initial	2019-10-24 15:14:07.319971+02
4	admin	0002_logentry_remove_auto_add	2019-10-24 15:14:07.352953+02
5	contenttypes	0002_remove_content_type_name	2019-10-24 15:14:07.408277+02
6	auth	0002_alter_permission_name_max_length	2019-10-24 15:14:07.430424+02
7	auth	0003_alter_user_email_max_length	2019-10-24 15:14:07.463747+02
8	auth	0004_alter_user_username_opts	2019-10-24 15:14:07.488227+02
9	auth	0005_alter_user_last_login_null	2019-10-24 15:14:07.519131+02
10	auth	0006_require_contenttypes_0002	2019-10-24 15:14:07.530316+02
11	auth	0007_alter_validators_add_error_messages	2019-10-24 15:14:07.551973+02
12	auth	0008_alter_user_username_max_length	2019-10-24 15:14:07.630111+02
13	sessions	0001_initial	2019-10-24 15:14:07.807443+02
14	hive	0001_initial	2019-10-25 13:35:38.735469+02
15	hive	0002_newsletterrecipients	2019-10-30 10:15:08.155586+02
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
d2ffysanxzllbu64ab3d0dyx8nbsv2ik	MDJmYWRiZmFkNjliY2FlNWExOGNkMjZkOWE1NTczZjMwZmRmN2RiODp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWM5ODlhYmFkNWY1ZWZiZGEwYjEwMWU0NTVjZjE4ZDZjMjIyZDZlIn0=	2019-11-13 14:03:24.827766+02
\.


--
-- Data for Name: hive_academic; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.hive_academic (id, academic_name, academic_location, academic_email) FROM stdin;
\.


--
-- Data for Name: hive_business; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.hive_business (id, business_founder, business_name, business_location, business_email) FROM stdin;
1	d	c	Kacyiru	umugeni@gmail.com
\.


--
-- Data for Name: hive_enterprise; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.hive_enterprise (id, enterprise_founder, enterprise_name, enterprise_location, entrprise_email) FROM stdin;
1	c	g	kigali	bayizere123@gmail.com
2	c	g	kigali	bayizere123@gmail.com
\.


--
-- Data for Name: hive_freelancer; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.hive_freelancer (id, freelancer_names, project_name, freelancer_email) FROM stdin;
\.


--
-- Data for Name: hive_government; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.hive_government (id, institution_name, institution_location, institution_adress) FROM stdin;
1	g	n	98
\.


--
-- Data for Name: hive_image; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.hive_image (id, images, title, description) FROM stdin;
\.


--
-- Data for Name: hive_newsletterrecipients; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.hive_newsletterrecipients (id, name, email) FROM stdin;
\.


--
-- Data for Name: hive_student; Type: TABLE DATA; Schema: public; Owner: bayizere
--

COPY public.hive_student (id, first_name, last_name, education_level, student_email) FROM stdin;
1	christine	bayizere	A0	bayizerechristine4@gmail.com
2	christine	bayizere	A0	bayizerechristine4@gmail.com
3	christine	bayizere	A0	bayizerechristine4@gmail.com
4	christine	christine	A0	bayizerechristine4@gmail.com
5	christine	bayizere	A0	bayizerechristine4@gmail.com
6	claudine	akimanizanye	A0	akimanizanye@akikahive.com
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 42, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 7, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 2, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 15, true);


--
-- Name: hive_academic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.hive_academic_id_seq', 1, false);


--
-- Name: hive_business_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.hive_business_id_seq', 1, true);


--
-- Name: hive_enterprise_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.hive_enterprise_id_seq', 2, true);


--
-- Name: hive_freelancer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.hive_freelancer_id_seq', 1, false);


--
-- Name: hive_government_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.hive_government_id_seq', 1, true);


--
-- Name: hive_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.hive_image_id_seq', 1, false);


--
-- Name: hive_newsletterrecipients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.hive_newsletterrecipients_id_seq', 1, false);


--
-- Name: hive_student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bayizere
--

SELECT pg_catalog.setval('public.hive_student_id_seq', 6, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: hive_academic hive_academic_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_academic
    ADD CONSTRAINT hive_academic_pkey PRIMARY KEY (id);


--
-- Name: hive_business hive_business_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_business
    ADD CONSTRAINT hive_business_pkey PRIMARY KEY (id);


--
-- Name: hive_enterprise hive_enterprise_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_enterprise
    ADD CONSTRAINT hive_enterprise_pkey PRIMARY KEY (id);


--
-- Name: hive_freelancer hive_freelancer_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_freelancer
    ADD CONSTRAINT hive_freelancer_pkey PRIMARY KEY (id);


--
-- Name: hive_government hive_government_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_government
    ADD CONSTRAINT hive_government_pkey PRIMARY KEY (id);


--
-- Name: hive_image hive_image_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_image
    ADD CONSTRAINT hive_image_pkey PRIMARY KEY (id);


--
-- Name: hive_newsletterrecipients hive_newsletterrecipients_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_newsletterrecipients
    ADD CONSTRAINT hive_newsletterrecipients_pkey PRIMARY KEY (id);


--
-- Name: hive_student hive_student_pkey; Type: CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.hive_student
    ADD CONSTRAINT hive_student_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: bayizere
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: bayizere
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

