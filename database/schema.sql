-- WARNING: This schema is for context only and is not meant to be run.
-- Table order and constraints may not be valid for execution.

CREATE TABLE public.agent_actions (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  ticket_id text,
  action text NOT NULL,
  type text NOT NULL CHECK (type = ANY (ARRAY['action'::text, 'decision'::text, 'reply'::text, 'escalation'::text, 'resolved'::text])),
  icon text DEFAULT '⚙️'::text,
  created_at timestamp with time zone DEFAULT now(),
  CONSTRAINT agent_actions_pkey PRIMARY KEY (id),
  CONSTRAINT agent_actions_ticket_id_fkey FOREIGN KEY (ticket_id) REFERENCES public.tickets(id)
);
CREATE TABLE public.messages (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  ticket_id text NOT NULL,
  role text NOT NULL CHECK (role = ANY (ARRAY['client'::text, 'agent'::text, 'human'::text])),
  is_ai boolean DEFAULT false,
  text text NOT NULL,
  created_at timestamp with time zone DEFAULT now(),
  CONSTRAINT messages_pkey PRIMARY KEY (id),
  CONSTRAINT messages_ticket_id_fkey FOREIGN KEY (ticket_id) REFERENCES public.tickets(id)
);
CREATE TABLE public.orders (
  order_ref text NOT NULL,
  product_name text NOT NULL,
  price numeric NOT NULL,
  order_date timestamp with time zone DEFAULT now(),
  carrier text,
  shipping_status text,
  tracking_url text,
  CONSTRAINT orders_pkey PRIMARY KEY (order_ref)
);
CREATE TABLE public.profiles (
  id uuid NOT NULL,
  role text NOT NULL CHECK (role = ANY (ARRAY['vendeur'::text, 'marketplace'::text])),
  company_name text,
  marketplace_name text,
  avatar character DEFAULT 'U'::bpchar,
  created_at timestamp with time zone DEFAULT now(),
  CONSTRAINT profiles_pkey PRIMARY KEY (id),
  CONSTRAINT profiles_id_fkey FOREIGN KEY (id) REFERENCES auth.users(id)
);
CREATE TABLE public.stock (
  product_name text NOT NULL,
  sku text,
  quantity_available integer NOT NULL DEFAULT 0,
  warehouse_location text,
  CONSTRAINT stock_pkey PRIMARY KEY (product_name)
);
CREATE TABLE public.tickets (
  id text NOT NULL DEFAULT ('TK-'::text || lpad((nextval('ticket_seq'::regclass))::text, 4, '0'::text)),
  vendor_id uuid,
  client text NOT NULL,
  email text,
  marketplace text NOT NULL,
  subject text NOT NULL,
  status text NOT NULL DEFAULT 'open'::text CHECK (status = ANY (ARRAY['open'::text, 'pending'::text, 'escalated'::text, 'resolved'::text])),
  priority text NOT NULL DEFAULT 'medium'::text CHECK (priority = ANY (ARRAY['critical'::text, 'high'::text, 'medium'::text, 'low'::text])),
  category text,
  assignee text DEFAULT 'Agent IA'::text,
  order_ref text,
  sla text,
  raw_message text,
  created_at timestamp with time zone DEFAULT now(),
  updated_at timestamp with time zone DEFAULT now(),
  intent text,
  urgency text DEFAULT 'standard'::text,
  country text DEFAULT 'FR'::text,
  ai_response text,
  requires_human boolean DEFAULT false,
  resolved_at timestamp with time zone,
  channel text DEFAULT 'marketplace'::text,
  CONSTRAINT tickets_pkey PRIMARY KEY (id),
  CONSTRAINT tickets_vendor_id_fkey FOREIGN KEY (vendor_id) REFERENCES public.profiles(id)
);
CREATE TABLE public.validations (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  ticket_id text,
  client text,
  marketplace text,
  amount numeric NOT NULL,
  type text NOT NULL,
  context text,
  agent_quote text,
  priority text CHECK (priority = ANY (ARRAY['critical'::text, 'high'::text, 'medium'::text, 'low'::text])),
  sla text,
  status text DEFAULT 'pending'::text CHECK (status = ANY (ARRAY['pending'::text, 'approved'::text, 'rejected'::text])),
  reject_reason text,
  resolved_by uuid,
  created_at timestamp with time zone DEFAULT now(),
  CONSTRAINT validations_pkey PRIMARY KEY (id),
  CONSTRAINT validations_ticket_id_fkey FOREIGN KEY (ticket_id) REFERENCES public.tickets(id),
  CONSTRAINT validations_resolved_by_fkey FOREIGN KEY (resolved_by) REFERENCES public.profiles(id)
);