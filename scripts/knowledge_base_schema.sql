-- Knowledge Base Database Schema
-- This schema provides a foundation for a flexible knowledge base system

-- 1. Main knowledge base table
-- Stores the core knowledge items with metadata
CREATE TABLE knowledge_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    category TEXT,
    tags TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    version INTEGER DEFAULT 1,
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'draft', 'archived')),
    author TEXT,
    source_url TEXT,
    is_published BOOLEAN DEFAULT 0
);

-- 2. Knowledge base metadata table
-- Stores additional information about knowledge items
CREATE TABLE knowledge_metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    knowledge_id INTEGER NOT NULL,
    key TEXT NOT NULL,
    value TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (knowledge_id) REFERENCES knowledge_base(id) ON DELETE CASCADE,
    UNIQUE(knowledge_id, key)
);

-- 3. Knowledge base relationships table
-- Defines relationships between knowledge items
CREATE TABLE knowledge_relationships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_knowledge_id INTEGER NOT NULL,
    target_knowledge_id INTEGER NOT NULL,
    relationship_type TEXT NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source_knowledge_id) REFERENCES knowledge_base(id) ON DELETE CASCADE,
    FOREIGN KEY (target_knowledge_id) REFERENCES knowledge_base(id) ON DELETE CASCADE,
    UNIQUE(source_knowledge_id, target_knowledge_id, relationship_type)
);

-- 4. Knowledge base version history
-- Tracks changes to knowledge items over time
CREATE TABLE knowledge_version_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    knowledge_id INTEGER NOT NULL,
    version_number INTEGER NOT NULL,
    title TEXT,
    content TEXT,
    changes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    author TEXT,
    FOREIGN KEY (knowledge_id) REFERENCES knowledge_base(id) ON DELETE CASCADE,
    UNIQUE(knowledge_id, version_number)
);

-- 5. Search index table
-- Optimized for fast text searches
CREATE TABLE search_index (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    knowledge_id INTEGER NOT NULL,
    search_text TEXT NOT NULL,
    word TEXT NOT NULL,
    position INTEGER NOT NULL,
    FOREIGN KEY (knowledge_id) REFERENCES knowledge_base(id) ON DELETE CASCADE
);

-- 6. User access and permissions
-- Manages who can view, edit, or delete knowledge items
CREATE TABLE user_permissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    knowledge_id INTEGER NOT NULL,
    user_id TEXT NOT NULL,
    permission_type TEXT NOT NULL,
    granted_by TEXT,
    granted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (knowledge_id) REFERENCES knowledge_base(id) ON DELETE CASCADE
);

-- 7. Audit log
-- Tracks all changes to the knowledge base
CREATE TABLE audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT NOT NULL,
    table_name TEXT NOT NULL,
    record_id INTEGER,
    old_values TEXT,
    new_values TEXT,
    user_id TEXT,
    ip_address TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_knowledge_base_title ON knowledge_base(title);
CREATE INDEX idx_knowledge_base_category ON knowledge_base(category);
CREATE INDEX idx_knowledge_base_tags ON knowledge_base(tags);
CREATE INDEX idx_knowledge_base_status ON knowledge_base(status);
CREATE INDEX idx_knowledge_base_published ON knowledge_base(is_published);
CREATE INDEX idx_knowledge_metadata_key ON knowledge_metadata(key);
CREATE INDEX idx_knowledge_relationships_source ON knowledge_relationships(source_knowledge_id);
CREATE INDEX idx_knowledge_relationships_target ON knowledge_relationships(target_knowledge_id);
CREATE INDEX idx_search_index_search_text ON search_index(search_text);
CREATE INDEX idx_search_index_word ON search_index(word);
CREATE INDEX idx_audit_log_timestamp ON audit_log(timestamp);

-- Triggers for automatic updates
CREATE TRIGGER update_updated_at 
AFTER UPDATE ON knowledge_base
BEGIN
    UPDATE knowledge_base SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

-- Create a view for published knowledge items
CREATE VIEW published_knowledge AS
SELECT id, title, content, category, tags, created_at, updated_at, author, source_url
FROM knowledge_base
WHERE status = 'active' AND is_published = 1;