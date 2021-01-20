CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  manager_lvl1_id INT,
  manager_lvl2_id INT,
  commercial_id INT,
  CONSTRAINT fk_manager_lvl1 FOREIGN KEY(manager_lvl1_id) REFERENCES users(id),
  CONSTRAINT fk_manager_lvl2 FOREIGN KEY(manager_lvl2_id) REFERENCES users(id),
  CONSTRAINT fk_commercial FOREIGN KEY(commercial_id) REFERENCES users(id)
);

CREATE TABLE facilities(
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  address TEXT
);

CREATE TABLE logs(
  id SERIAL PRIMARY KEY,
  facility_id INT NOT NULL,
  user_id INT, /* If NULL, log is a system log */
  content TEXT NOT NULL,
  date TIMESTAMP,
  CONSTRAINT fk_facility FOREIGN KEY(facility_id) REFERENCES facilities(id),
  CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(id)
);
