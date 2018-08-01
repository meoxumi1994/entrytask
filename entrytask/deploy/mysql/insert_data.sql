USE event_sharing_db;

INSERT INTO user_tab value(NULL, 'user_name', 'password', 'address', 1533024509, 'full_name', true, 'visitor', 'email', 'salt', 'avatar', 'create_by');

INSERT INTO category_tab value(NULL, 'coffee', 1533024509, 'description ...', 'category_photo' );
INSERT INTO category_tab value(NULL, 'tea', 1533024509, 'description ...', 'category_photo' );
INSERT INTO category_tab value(NULL, 'beer', 1533024509, 'description ...', 'category_photo' );
INSERT INTO category_tab value(NULL, 'travel', 1533024509, 'description ...', 'category_photo' );
INSERT INTO category_tab value(NULL, 'film', 1533024509, 'description ...', 'category_photo' );
INSERT INTO category_tab value(NULL, 'dance', 1533024509, 'description ...', 'category_photo' );
INSERT INTO category_tab value(NULL, 'bar', 1533024509, 'description ...', 'category_photo' );
INSERT INTO category_tab value(NULL, 'restaurant', 1533024509, 'description ...', 'category_photo' );
INSERT INTO category_tab value(NULL, 'beach', 1533024509, 'description ...', 'category_photo' );

INSERT INTO tag_tab value(NULL, 'coffee', 1533024509);
INSERT INTO tag_tab value(NULL, 'tea', 1533024509);
INSERT INTO tag_tab value(NULL, 'beer', 1533024509);
INSERT INTO tag_tab value(NULL, 'travel', 1533024509);
INSERT INTO tag_tab value(NULL, 'film', 1533024509);
INSERT INTO tag_tab value(NULL, 'dance', 1533024509);
INSERT INTO tag_tab value(NULL, 'bar', 1533024509);
INSERT INTO tag_tab value(NULL, 'restaurant', 1533024509);
INSERT INTO tag_tab value(NULL, 'beach', 1533024509);



INSERT INTO event_tab value(NULL, 1, 1533021509, 1533021509, 'hanoi', 'title', 'description', 1);
INSERT INTO event_tab value(NULL, 1, 1533022509, 1533022509, 'hanoi', 'title', 'description', 1);
INSERT INTO event_tab value(NULL, 1, 1533023509, 1533023509, 'hanoi', 'title', 'description', 2);
INSERT INTO event_tab value(NULL, 1, 1533024509, 1533024509, 'hanoi', 'title', 'description', 2);

INSERT INTO event_tag_tab value(NULL, 1 ,1 );
INSERT INTO event_tag_tab value(NULL, 2 ,1 );
INSERT INTO event_tag_tab value(NULL, 3 ,1 );

INSERT INTO photo_tab value(NULL, '/2018-07-29/2d44a40ffd3fbc1fd205f87f9dae9ee3eeeed8a4018fb2ee1709253e6ad5da9688ee0739e8c449d9579b7863638976edf2da0925396a8b57516c27dae96005ca.png', 'coffee image', 1533024509, 1);
INSERT INTO photo_tab value(NULL, '/2018-07-29/2d44a40ffd3fbc1fd205f87f9dae9ee3eeeed8a4018fb2ee1709253e6ad5da9688ee0739e8c449d9579b7863638976edf2da0925396a8b57516c27dae96005ca.png', 'hanoi image', 1533024509, 1);
INSERT INTO photo_tab value(NULL, '/2018-07-29/2d44a40ffd3fbc1fd205f87f9dae9ee3eeeed8a4018fb2ee1709253e6ad5da9688ee0739e8c449d9579b7863638976edf2da0925396a8b57516c27dae96005ca.png', 'caro image', 1533024509, 1);
