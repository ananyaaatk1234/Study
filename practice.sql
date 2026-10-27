CREATE TABLE machines( 
    SrNo int PRIMARY KEY,
    Mach_name VARCHAR(100),
    Mach_id VARCHAR(20));

INSERT into machines
    (SrNo, Mach_name, Mach_id)
VALUES  
    (1, 'Machine_1', 'M001');
INSERT into machines
    (SrNo, Mach_name, Mach_id)
VALUES  
    (2, 'Machine_2', 'M002');
INSERT into machines
    (SrNo, Mach_name, Mach_id)
VALUES  
    (3, 'Machine_3', 'M003');

SELECT * FROM machines;