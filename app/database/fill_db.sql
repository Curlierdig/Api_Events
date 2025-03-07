-- First, insert organizers
INSERT INTO torganizers (name, contact, logo) VALUES
('Gobierno Municipal de Chihuahua', 'eventos@chihuahua.gob.mx', 'https://example.com/logos/gobierno_chihuahua.png'),
('Universidad Autónoma de Chihuahua', 'eventos@uach.mx', 'https://example.com/logos/uach.png'),
('Teatro de la Ciudad', 'contacto@teatrodelaciudad.mx', 'https://example.com/logos/teatro_ciudad.png'),
('Casa Chihuahua', 'eventos@casachihuahua.org', 'https://example.com/logos/casa_chihuahua.png'),
('Centro de Convenciones Expo Chihuahua', 'info@expochihuahua.com', 'https://example.com/logos/expo_chihuahua.png'),
('Conservatorio de Música de Chihuahua', 'eventos@conservatoriochihuahua.edu.mx', 'https://example.com/logos/conservatorio.png'),
('Plaza Mayor Centro Comercial', 'eventos@plazamayor.mx', 'https://example.com/logos/plaza_mayor.png'),
('Parque El Palomar', 'parques@chihuahua.gob.mx', 'https://example.com/logos/parque_palomar.png'),
('Deportes Chihuahua', 'contacto@deporteschihuahua.mx', 'https://example.com/logos/deportes_chihuahua.png'),
('Fundación Cultural Chihuahua', 'contacto@fundacionculturalchihuahua.org', 'https://example.com/logos/fundacion_cultural.png'),
('Biblioteca Central Carlos Montemayor', 'info@bibliotecamontemayor.mx', 'https://example.com/logos/biblioteca_montemayor.png'),
('Festival Internacional Chihuahua', 'contacto@fichihuahua.mx', 'https://example.com/logos/fichihuahua.png'),
('Centro Cultural Quinta Gameros', 'eventos@quintagameros.mx', 'https://example.com/logos/quinta_gameros.png'),
('Museo Semilla', 'info@museosemilla.mx', 'https://example.com/logos/museo_semilla.png'),
('Foro Cultural Independiente', 'contacto@forocultural.mx', 'https://example.com/logos/foro_cultural.png'),
('Centro de Desarrollo Cultural', 'eventos@cdcchihuahua.mx', 'https://example.com/logos/centro_desarrollo.png'),
('Museo de la Revolución Mexicana', 'info@museorevolucion.mx', 'https://example.com/logos/museo_revolucion.png'),
('Universidad Tecnológica de Chihuahua', 'eventos@utch.mx', 'https://example.com/logos/utch.png'),
('Asociación de Escritores de Chihuahua', 'contacto@escritoreschihuahua.mx', 'https://example.com/logos/escritores.png'),
('Orquesta Filarmónica del Estado', 'info@filarmonicachihuahua.mx', 'https://example.com/logos/filarmonica.png'),
('Centro de Espectáculos Chihuahua', 'eventos@espectaculoschihuahua.mx', 'https://example.com/logos/centro_espectaculos.png'),
('Centro Deportivo Norte', 'contacto@centronorte.mx', 'https://example.com/logos/deportivo_norte.png'),
('Centro Histórico de Chihuahua', 'info@centrohistorico.mx', 'https://example.com/logos/centro_historico.png'),
('Parque Metropolitano Tres Presas', 'parques@chihuahua.gob.mx', 'https://example.com/logos/parque_tres_presas.png'),
('Centro de Innovación y Emprendimiento', 'info@ciechihuahua.mx', 'https://example.com/logos/centro_innovacion.png');

-- Insert locations in Chihuahua city
INSERT INTO tlocations (address, lat, lng) VALUES
('Plaza de Armas, Centro, Chihuahua', 28.6353, -106.0889),
('Av. Universidad y C. Escorza, Chihuahua', 28.6372, -106.0754),
('C. Ojinaga 901, Centro, Chihuahua', 28.6379, -106.0926),
('Av. Venustiano Carranza 807, Centro, Chihuahua', 28.6346, -106.0755),
('Av. Tecnológico 1405, Santo Niño, Chihuahua', 28.6583, -106.0996),
('C. Libertad 601, Centro, Chihuahua', 28.6363, -106.0894),
('Periférico de la Juventud 6902, Chihuahua', 28.6825, -106.1493),
('Blvd. Antonio Ortiz Mena, Chihuahua', 28.6622, -106.1100),
('Estadio Olímpico Universitario, Chihuahua', 28.6343, -106.0847),
('Av. División del Norte, Altavista, Chihuahua', 28.6511, -106.1075),
('Parque El Palomar, Chihuahua', 28.6528, -106.0894),
('Quinta Gameros, Chihuahua', 28.6410, -106.0795),
('Museo Casa Chihuahua, Chihuahua', 28.6373, -106.0890),
('Mediateca Municipal, Chihuahua', 28.6354, -106.0856),
('Deportiva Sur, Chihuahua', 28.6200, -106.0794),
('C. Libertad 1301, Centro, Chihuahua', 28.6389, -106.0862),
('Av. Universidad 1201, Chihuahua', 28.6415, -106.0733),
('C. 5ta y Jiménez, Centro, Chihuahua', 28.6322, -106.0897),
('Av. Niños Héroes 1101, Chihuahua', 28.6401, -106.0768),
('C. Victoria 812, Centro, Chihuahua', 28.6366, -106.0865),
('Blvd. Ortiz Mena 3201, Chihuahua', 28.6654, -106.1157),
('C. 20 de Noviembre 1801, Chihuahua', 28.6392, -106.0834),
('Av. Vallarta 1505, Chihuahua', 28.6563, -106.0998),
('Periférico R. Almada 8900, Chihuahua', 28.5912, -106.0842),
('C. Morelos 901, Centro, Chihuahua', 28.6399, -106.0860),
('Parque Revolución, Chihuahua', 28.6471, -106.0762),
('Centro Deportivo Tricentenario, Chihuahua', 28.7021, -106.1314),
('Museo de Arte Sacro, Chihuahua', 28.6358, -106.0811),
('Plaza del Ángel, Chihuahua', 28.6369, -106.0880),
('Estadio Manuel L. Almanza, Chihuahua', 28.6418, -106.0921);

-- Insert event data (100 events)
-- First, let's create a procedure to generate the events
DELIMITER //
CREATE PROCEDURE GenerateEvents()
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE event_date DATE;
    DECLARE event_name VARCHAR(100);
    DECLARE event_type INT;
    DECLARE event_location INT;
    DECLARE event_organizer INT;
    DECLARE event_budget DECIMAL(10, 2);
    DECLARE is_featured BOOLEAN;
    
    -- Clear any existing events for clean run
    DELETE FROM tevents;
    
    WHILE i < 100 DO
        -- Generate a random date in the next 9 months
        SET event_date = DATE_ADD(CURDATE(), INTERVAL FLOOR(RAND() * 270) DAY);
        
        -- Select random type, location, and organizer
        SET event_type = FLOOR(RAND() * 10) + 1;
        SET event_location = FLOOR(RAND() * 30) + 1;
        SET event_organizer = FLOOR(RAND() * 25) + 1;
        SET event_budget = ROUND(RAND() * 5000 + 0, 2);
        SET is_featured = IF(RAND() > 0.8, TRUE, FALSE);
        
        -- Create event name based on type
        CASE event_type
            WHEN 1 THEN SET event_name = CONCAT('Concierto ', 
                ELT(FLOOR(RAND() * 10) + 1, 
                    'Filarmónica de Chihuahua', 
                    'Bandas Locales en el Parque', 
                    'Rock Sinfónico', 
                    'Música Norteña en la Plaza', 
                    'Jazz bajo las Estrellas', 
                    'Recital de Piano', 
                    'Voces Chihuahuenses', 
                    'Guitarra Clásica', 
                    'Música Regional Mexicana', 
                    'de Música Contemporánea'));
            WHEN 2 THEN SET event_name = CONCAT('Festival ', 
                ELT(FLOOR(RAND() * 10) + 1, 
                    'de Cine Chihuahuense', 
                    'Gastronómico de la Frontera Norte', 
                    'Cultural de la Ciudad', 
                    'de Danza Contemporánea', 
                    'Internacional de Teatro', 
                    'de las Artes', 
                    'del Desierto', 
                    'de la Cerveza Artesanal', 
                    'Folklórico de Chihuahua', 
                    'de Primavera'));
            WHEN 3 THEN SET event_name = CONCAT('Conferencia sobre ', 
                ELT(FLOOR(RAND() * 10) + 1, 
                    'Historia de Chihuahua', 
                    'Desarrollo Económico Regional', 
                    'Tecnologías Emergentes', 
                    'Sustentabilidad en el Desierto', 
                    'Patrimonio Cultural Chihuahuense', 
                    'Industria y Comercio', 
                    'Arte Contemporáneo', 
                    'Educación y Sociedad', 
                    'Turismo en el Norte de México', 
                    'Innovación Empresarial'));
            WHEN 4 THEN SET event_name = CONCAT('Exposición de ', 
                ELT(FLOOR(RAND() * 10) + 1, 
                    'Fotografía Histórica', 
                    'Arte Contemporáneo', 
                    'Artesanías Regionales', 
                    'Esculturas en Metal', 
                    'Pintores Chihuahuenses', 
                    'Arte Tarahumara', 
                    'Historia Minera', 
                    'Tecnología e Innovación', 
                    'Diseño Industrial', 
                    'Biodiversidad del Desierto'));
            WHEN 5 THEN SET event_name = CONCAT('Fiesta ', 
                ELT(FLOOR(RAND() * 10) + 1, 
                    'Mexicana en la Plaza', 
                    'de la Independencia', 
                    'de la Revolución', 
                    'Cultural Chihuahuense', 
                    'de la Primavera', 
                    'de Verano en el Parque', 
                    'del Estudiante', 
                    'Tradicional', 
                    'del Barrio Histórico', 
                    'de la Música y Danza'));
            WHEN 6 THEN SET event_name = CONCAT('Teatro: ', 
                ELT(FLOOR(RAND() * 10) + 1, 
                    'La Casa de Bernarda Alba', 
                    'Bodas de Sangre', 
                    'El Gesticulador', 
                    'La Dama de Negro', 
                    'Cuentos de Frontera', 
                    'Sueño de una Noche de Verano', 
                    'Las Historias de Chihuahua', 
                    'El Juego que Todos Jugamos', 
                    'Don Quijote en el Norte', 
                    'Antígona'));
            WHEN 7 THEN SET event_name = CONCAT('Evento Deportivo: ', 
                ELT(FLOOR(RAND() * 10) + 1, 
                    'Maratón Chihuahua', 
                    'Torneo de Fútbol Universitario', 
                    'Copa Chihuahua de Baloncesto', 
                    'Ciclismo Urbano', 
                    'Carrera 10K por la Ciudad', 
                    'Exhibición de Artes Marciales', 
                    'Torneo de Tenis Municipal', 
                    'Competencia de Natación', 
                    'Triatlón del Desierto', 
                    'Partido de Béisbol Local'));
            WHEN 8 THEN SET event_name = CONCAT('Evento Cultural: ', 
                ELT(FLOOR(RAND() * 10) + 1, 
                    'Danzas Tradicionales de Chihuahua', 
                    'Muestra Gastronómica Regional', 
                    'Poesía bajo las Estrellas', 
                    'Noche de Museos', 
                    'Cuenta Cuentos para Niños', 
                    'Recorrido Histórico por el Centro', 
                    'Taller de Artesanías Locales', 
                    'Conmemoración Histórica', 
                    'Feria del Libro Chihuahuense', 
                    'Encuentro de Culturas Indígenas'));
            WHEN 9 THEN SET event_name = CONCAT('Festival Gastronómico: ', 
                ELT(FLOOR(RAND() * 10) + 1, 
                    'Sabores de Chihuahua', 
                    'La Ruta del Queso Menonita', 
                    'Festival de la Carne Asada', 
                    'Muestra de Chiles y Salsas', 
                    'La Ruta del Sotol', 
                    'Cocina Tradicional del Norte', 
                    'Festival de la Tortilla', 
                    'Dulces Regionales', 
                    'Mercado de Productores Locales', 
                    'Festival del Manzano'));
            WHEN 10 THEN SET event_name = CONCAT('Evento Educativo: ', 
                ELT(FLOOR(RAND() * 10) + 1, 
                    'Feria de Ciencias UACH', 
                    'Taller de Robótica para Jóvenes', 
                    'Semana de la Ingeniería', 
                    'Congreso de Educación', 
                    'Seminario de Historia Regional', 
                    'Taller de Escritura Creativa', 
                    'Concurso de Matemáticas', 
                    'Feria de Orientación Vocacional', 
                    'Simposio de Investigación', 
                    'Taller de Innovación'));
        END CASE;

        -- Insert the event
        INSERT INTO tevents (name, date, time, type_id, budget, description, image, location_id, organizer_id, featured)
        VALUES (
            event_name,
            event_date,
            MAKETIME(FLOOR(RAND() * 12) + 8, FLOOR(RAND() * 4) * 15, 0), -- Random time between 8 AM and 8 PM
            event_type,
            event_budget,
            CASE event_type
                WHEN 1 THEN CONCAT('Disfruta de una experiencia musical única con los mejores talentos de la región. ', 
                    'Un evento imperdible para los amantes de la música en Chihuahua.')
                WHEN 2 THEN CONCAT('Festival que reúne lo mejor de la cultura y el entretenimiento. ',
                    'Una celebración para toda la familia con actividades durante todo el día.')
                WHEN 3 THEN CONCAT('Expertos compartirán conocimientos y experiencias sobre temas relevantes para nuestra sociedad. ',
                    'Una oportunidad para el aprendizaje y el debate constructivo.')
                WHEN 4 THEN CONCAT('Exposición que muestra el talento y la creatividad de artistas locales e internacionales. ',
                    'Una ventana al arte y la cultura en el corazón de Chihuahua.')
                WHEN 5 THEN CONCAT('Celebración con música, baile y gastronomía típica de nuestra región. ',
                    'Ven a disfrutar de una noche llena de alegría y tradición.')
                WHEN 6 THEN CONCAT('Presentación teatral que te llevará a través de emociones y reflexiones. ',
                    'Una obra interpretada por talentosos actores que te dejará sin aliento.')
                WHEN 7 THEN CONCAT('Evento deportivo que promueve la actividad física y la competencia sana. ',
                    'Participa o disfruta como espectador de este emocionante evento.')
                WHEN 8 THEN CONCAT('Celebración de nuestras raíces y tradiciones culturales. ',
                    'Un espacio para valorar y preservar el patrimonio cultural de Chihuahua.')
                WHEN 9 THEN CONCAT('Un recorrido por los sabores más auténticos de la cocina chihuahuense. ',
                    'Degustación de platillos típicos preparados por chefs locales.')
                WHEN 10 THEN CONCAT('Evento enfocado en el aprendizaje y desarrollo de habilidades. ',
                    'Una oportunidad para expandir conocimientos y fomentar la curiosidad intelectual.')
            END,
            CONCAT('https://example.com/events/images/chihuahua_', i + 1, '.jpg'),
            event_location,
            event_organizer,
            is_featured
        );
        
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

-- Execute the procedure
CALL GenerateEvents();

-- Drop the procedure after use
DROP PROCEDURE GenerateEvents;