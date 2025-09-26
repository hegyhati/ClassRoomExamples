
Entities:
    User (id, email, size)
    Purchase (id, user_id, costume_id, timestamp)
    Costume (id, name, character, movie_id)
    Offer (id, user_id, costume_id, sent_at, expires_at, used)
    Friendship (user_id, friend_id)
    Page (id, name, category)
    Follow (user_id, page_id)
    Movie (id, title, release_date)
    Actor (id, name)
    Role (actor_id, movie_id, character_name)
Relationships:
    User ↔ Purchase (1:N)
    User ↔ Offer (1:N)
    User ↔ Friendship (M:N via Friendship)
    User ↔ Page (M:N via Follow)
    Costume ↔ Movie (N:1)
    Actor ↔ Movie (M:N via Role)


