test_data = {
    "ivs": {
        "ys": [
            6640, 6670, 6670, 6640, 6670, 6670, 6640, 6640, 6640, 6640, 6640, 6640, 6640, 6640, 6640, 6640, 6620, 6640, 6640, 6640, 6620, 6620, 6620, 6640, 6640, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6640, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6600, 6600, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6620, 6600, 6600, 6600, 6600, 6600, 6600, 6600, 6570, 6570, 6570, 6570, 6600, 6570, 6600, 6600, 6600, 6600, 6600, 6600, 6600, 6600, 6600, 6600, 6600, 6600, 6570, 6570, 6600, 6570, 6570, 6570, 6570, 6570, 6570, 6570, 6550, 6500, 6480, 6480, 6480, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6410, 6410, 6410, 6410, 6410, 6410, 6410, 6410, 6410, 6410, 6410, 6410, 6430, 6460, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6460, 6480, 6480, 6460, 6480, 6460, 6460, 6480, 6460, 6480, 6460, 6460, 6460, 6480, 6480, 6480, 6480, 6480, 6480, 6500, 6500, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6460, 6460, 6460, 6480, 6500, 6500, 6530, 6530, 6530, 6530, 6500, 6530, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6530, 6530, 6530, 6530, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6530, 6500, 6530, 6500, 6500, 6530, 6500, 6530, 6530, 6500, 6500, 6500, 6500, 6500, 6530, 6500, 6530, 6530, 6530, 6530, 6530, 6530, 6530, 6530, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6530, 6530, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6530, 6530, 6530, 6530, 6530, 6530, 6530, 6530, 6530, 6530, 6500, 6500, 6530, 6500, 6530, 6530, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6460, 6460, 6460, 6460, 6480, 6480, 6480, 6480, 6480, 6500, 6500, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6480, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6480, 6480, 6500, 6480, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6530, 6500, 6500, 6530, 6530, 6530, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6530, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6530, 6530, 6530, 6530, 6500, 6530, 6530, 6530, 6500, 6530, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6530, 6500, 6500, 6500, 6530, 6570, 6570, 6570, 6570, 6570, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6550, 6500, 6480, 6460, 6460, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6460, 6480, 6500, 6500, 6500, 6480, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6460, 6430, 6430, 6430, 6430, 6430, 6410, 6430, 6430, 6430, 6460, 6460, 6430, 6430, 6430, 6460, 6430, 6430, 6460, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6430, 6410, 6430, 6430, 6430, 6430, 6430, 6410, 6430, 6480, 6480, 6480, 6500, 6500, 6480, 6530, 6570, 6600, 6600, 6690, 6740, 6790, 6790, 6810, 6810, 6810, 6830, 6810, 6830, 6810, 6810, 6830, 6810, 6810, 6810, 6810, 6810
            ],
        "xs": [
            "2018-03-30-21-30", "2018-03-30-21-45", "2018-03-30-22-00", "2018-03-30-22-15", "2018-03-30-22-30", "2018-03-30-22-45", "2018-03-30-23-00", "2018-03-30-23-15", "2018-03-30-23-30", "2018-03-30-23-45", "2018-03-31-00-00", "2018-03-31-00-15", "2018-03-31-00-30", "2018-03-31-00-45", "2018-03-31-01-00", "2018-03-31-01-15", "2018-03-31-01-30", "2018-03-31-01-45", "2018-03-31-02-00", "2018-03-31-02-15", "2018-03-31-02-30", "2018-03-31-02-45", "2018-03-31-03-00", "2018-03-31-03-15", "2018-03-31-03-30", "2018-03-31-03-45", "2018-03-31-04-00", "2018-03-31-04-15", "2018-03-31-04-30", "2018-03-31-04-45", "2018-03-31-05-00", "2018-03-31-05-15", "2018-03-31-05-30", "2018-03-31-05-45", "2018-03-31-06-00", "2018-03-31-06-15", "2018-03-31-06-30", "2018-03-31-06-45", "2018-03-31-07-00", "2018-03-31-07-15", "2018-03-31-07-30", "2018-03-31-07-45", "2018-03-31-08-00", "2018-03-31-08-15", "2018-03-31-08-30", "2018-03-31-08-45", "2018-03-31-09-00", "2018-03-31-09-15", "2018-03-31-09-30", "2018-03-31-09-45", "2018-03-31-10-00", "2018-03-31-10-15", "2018-03-31-10-30", "2018-03-31-10-45", "2018-03-31-11-00", "2018-03-31-11-15", "2018-03-31-11-30", "2018-03-31-11-45", "2018-03-31-12-00", "2018-03-31-12-15", "2018-03-31-12-30", "2018-03-31-12-45", "2018-03-31-13-00", "2018-03-31-13-15", "2018-03-31-13-30", "2018-03-31-13-45", "2018-03-31-14-00", "2018-03-31-14-15", "2018-03-31-14-30", "2018-03-31-14-45", "2018-03-31-15-00", "2018-03-31-15-15", "2018-03-31-15-30", "2018-03-31-15-45", "2018-03-31-16-00", "2018-03-31-16-15", "2018-03-31-16-30", "2018-03-31-16-45", "2018-03-31-17-00", "2018-03-31-17-15", "2018-03-31-17-30", "2018-03-31-17-45", "2018-03-31-18-00", "2018-03-31-18-15", "2018-03-31-18-30", "2018-03-31-18-45", "2018-03-31-19-00", "2018-03-31-19-15", "2018-03-31-19-30", "2018-03-31-19-45", "2018-03-31-20-00", "2018-03-31-20-15", "2018-03-31-20-30", "2018-03-31-20-45", "2018-03-31-21-00", "2018-03-31-21-15", "2018-03-31-21-30", "2018-03-31-21-45", "2018-03-31-22-00", "2018-03-31-22-15", "2018-03-31-22-30", "2018-03-31-22-45", "2018-03-31-23-00", "2018-03-31-23-15", "2018-03-31-23-30", "2018-03-31-23-45", "2018-04-01-00-00", "2018-04-01-00-15", "2018-04-01-00-30", "2018-04-01-00-45", "2018-04-01-01-00", "2018-04-01-01-15", "2018-04-01-01-30", "2018-04-01-01-45", "2018-04-01-02-00", "2018-04-01-02-15", "2018-04-01-02-30", "2018-04-01-02-45", "2018-04-01-03-00", "2018-04-01-03-15", "2018-04-01-03-30", "2018-04-01-03-45", "2018-04-01-04-00", "2018-04-01-04-15", "2018-04-01-04-30", "2018-04-01-04-45", "2018-04-01-05-00", "2018-04-01-05-15", "2018-04-01-05-30", "2018-04-01-05-45", "2018-04-01-06-00", "2018-04-01-06-15", "2018-04-01-06-30", "2018-04-01-06-45", "2018-04-01-07-00", "2018-04-01-07-15", "2018-04-01-07-30", "2018-04-01-07-45", "2018-04-01-08-00", "2018-04-01-08-15", "2018-04-01-08-30", "2018-04-01-08-45", "2018-04-01-09-00", "2018-04-01-09-15", "2018-04-01-09-30", "2018-04-01-09-45", "2018-04-01-10-00", "2018-04-01-10-15", "2018-04-01-10-30", "2018-04-01-10-45", "2018-04-01-11-00", "2018-04-01-11-15", "2018-04-01-11-30", "2018-04-01-11-45", "2018-04-01-12-00", "2018-04-01-12-15", "2018-04-01-12-30", "2018-04-01-12-45", "2018-04-01-13-00", "2018-04-01-13-15", "2018-04-01-13-30", "2018-04-01-13-45", "2018-04-01-14-00", "2018-04-01-14-15", "2018-04-01-14-30", "2018-04-01-14-45", "2018-04-01-15-00", "2018-04-01-15-15", "2018-04-01-15-30", "2018-04-01-15-45", "2018-04-01-16-00", "2018-04-01-16-15", "2018-04-01-16-30", "2018-04-01-16-45", "2018-04-01-17-00", "2018-04-01-17-15", "2018-04-01-17-30", "2018-04-01-17-45", "2018-04-01-18-00", "2018-04-01-18-15", "2018-04-01-18-30", "2018-04-01-18-45", "2018-04-01-19-00", "2018-04-01-19-15", "2018-04-01-19-30", "2018-04-01-19-45", "2018-04-01-20-00", "2018-04-01-20-15", "2018-04-01-20-30", "2018-04-01-20-45", "2018-04-01-21-00", "2018-04-01-21-15", "2018-04-01-21-30", "2018-04-01-21-45", "2018-04-01-22-00", "2018-04-01-22-15", "2018-04-01-22-30", "2018-04-01-22-45", "2018-04-01-23-00", "2018-04-01-23-15", "2018-04-01-23-30", "2018-04-01-23-45", "2018-04-02-00-00", "2018-04-02-00-15", "2018-04-02-00-30", "2018-04-02-00-45", "2018-04-02-01-00", "2018-04-02-01-15", "2018-04-02-01-30", "2018-04-02-01-45", "2018-04-02-02-00", "2018-04-02-02-15", "2018-04-02-02-30", "2018-04-02-02-45", "2018-04-02-03-00", "2018-04-02-03-15", "2018-04-02-03-30", "2018-04-02-03-45", "2018-04-02-04-00", "2018-04-02-04-15", "2018-04-02-04-30", "2018-04-02-04-45", "2018-04-02-05-00", "2018-04-02-05-15", "2018-04-02-05-30", "2018-04-02-05-45", "2018-04-02-06-00", "2018-04-02-06-15", "2018-04-02-06-30", "2018-04-02-06-45", "2018-04-02-07-00", "2018-04-02-07-15", "2018-04-02-07-30", "2018-04-02-07-45", "2018-04-02-08-00", "2018-04-02-08-15", "2018-04-02-08-30", "2018-04-02-08-45", "2018-04-02-09-00", "2018-04-02-09-15", "2018-04-02-09-30", "2018-04-02-09-45", "2018-04-02-10-00", "2018-04-02-10-15", "2018-04-02-10-30", "2018-04-02-10-45", "2018-04-02-11-00", "2018-04-02-11-15", "2018-04-02-11-30", "2018-04-02-11-45", "2018-04-02-12-00", "2018-04-02-12-15", "2018-04-02-12-30", "2018-04-02-12-45", "2018-04-02-13-00", "2018-04-02-13-15", "2018-04-02-13-30", "2018-04-02-13-45", "2018-04-02-14-00", "2018-04-02-14-15", "2018-04-02-14-30", "2018-04-02-14-45", "2018-04-02-15-00", "2018-04-02-15-15", "2018-04-02-15-30", "2018-04-02-15-45", "2018-04-02-16-00", "2018-04-02-16-15", "2018-04-02-16-30", "2018-04-02-16-45", "2018-04-02-17-00", "2018-04-02-17-15", "2018-04-02-17-30", "2018-04-02-17-45", "2018-04-02-18-00", "2018-04-02-18-15", "2018-04-02-18-30", "2018-04-02-18-45", "2018-04-02-19-00", "2018-04-02-19-15", "2018-04-02-19-30", "2018-04-02-19-45", "2018-04-02-20-00", "2018-04-02-20-15", "2018-04-02-20-30", "2018-04-02-20-45", "2018-04-02-21-00", "2018-04-02-21-15", "2018-04-02-21-30", "2018-04-02-21-45", "2018-04-02-22-00", "2018-04-02-22-15", "2018-04-02-22-30", "2018-04-02-22-45", "2018-04-02-23-00", "2018-04-02-23-15", "2018-04-02-23-30", "2018-04-02-23-45", "2018-04-03-00-00", "2018-04-03-00-15", "2018-04-03-00-30", "2018-04-03-00-45", "2018-04-03-01-00", "2018-04-03-01-15", "2018-04-03-01-30", "2018-04-03-01-45", "2018-04-03-02-00", "2018-04-03-02-15", "2018-04-03-02-30", "2018-04-03-02-45", "2018-04-03-03-00", "2018-04-03-03-15", "2018-04-03-03-30", "2018-04-03-03-45", "2018-04-03-04-00", "2018-04-03-04-15", "2018-04-03-04-30", "2018-04-03-04-45", "2018-04-03-05-00", "2018-04-03-05-15", "2018-04-03-05-30", "2018-04-03-05-45", "2018-04-03-06-00", "2018-04-03-06-15", "2018-04-03-06-30", "2018-04-03-06-45", "2018-04-03-07-00", "2018-04-03-07-15", "2018-04-03-07-30", "2018-04-03-07-45", "2018-04-03-08-00", "2018-04-03-08-15", "2018-04-03-08-30", "2018-04-03-08-45", "2018-04-03-09-00", "2018-04-03-09-15", "2018-04-03-09-30", "2018-04-03-09-45", "2018-04-03-10-00", "2018-04-03-10-15", "2018-04-03-10-30", "2018-04-03-10-45", "2018-04-03-11-00", "2018-04-03-11-15", "2018-04-03-11-30", "2018-04-03-11-45", "2018-04-03-12-00", "2018-04-03-12-15", "2018-04-03-12-30", "2018-04-03-12-45", "2018-04-03-13-00", "2018-04-03-13-15", "2018-04-03-13-30", "2018-04-03-13-45", "2018-04-03-14-00", "2018-04-03-14-15", "2018-04-03-14-30", "2018-04-03-14-45", "2018-04-03-15-00", "2018-04-03-15-15", "2018-04-03-15-30", "2018-04-03-15-45", "2018-04-03-16-00", "2018-04-03-16-15", "2018-04-03-16-30", "2018-04-03-16-45", "2018-04-03-17-00", "2018-04-03-17-15", "2018-04-03-17-30", "2018-04-03-17-45", "2018-04-03-18-00", "2018-04-03-18-15", "2018-04-03-18-30", "2018-04-03-18-45", "2018-04-03-19-00", "2018-04-03-19-15", "2018-04-03-19-30", "2018-04-03-19-45", "2018-04-03-20-00", "2018-04-03-20-15", "2018-04-03-20-30", "2018-04-03-20-45", "2018-04-03-21-00", "2018-04-03-21-15", "2018-04-03-21-30", "2018-04-03-21-45", "2018-04-03-22-00", "2018-04-03-22-15", "2018-04-03-22-30", "2018-04-03-22-45", "2018-04-03-23-00", "2018-04-03-23-15", "2018-04-03-23-30", "2018-04-03-23-45", "2018-04-04-00-00", "2018-04-04-00-15", "2018-04-04-00-30", "2018-04-04-00-45", "2018-04-04-01-00", "2018-04-04-01-15", "2018-04-04-01-30", "2018-04-04-01-45", "2018-04-04-02-00", "2018-04-04-02-15", "2018-04-04-02-30", "2018-04-04-02-45", "2018-04-04-03-00", "2018-04-04-03-15", "2018-04-04-03-30", "2018-04-04-03-45", "2018-04-04-04-00", "2018-04-04-04-15", "2018-04-04-04-30", "2018-04-04-04-45", "2018-04-04-05-00", "2018-04-04-05-15", "2018-04-04-05-30", "2018-04-04-05-45", "2018-04-04-06-00", "2018-04-04-06-15", "2018-04-04-06-30", "2018-04-04-06-45", "2018-04-04-07-00", "2018-04-04-07-15", "2018-04-04-07-30", "2018-04-04-07-45", "2018-04-04-08-00", "2018-04-04-08-15", "2018-04-04-08-30", "2018-04-04-08-45", "2018-04-04-09-00", "2018-04-04-09-15", "2018-04-04-09-30", "2018-04-04-09-45", "2018-04-04-10-00", "2018-04-04-10-15", "2018-04-04-10-30", "2018-04-04-10-45", "2018-04-04-11-00", "2018-04-04-11-15", "2018-04-04-11-30", "2018-04-04-11-45", "2018-04-04-12-00", "2018-04-04-12-15", "2018-04-04-12-30", "2018-04-04-12-45", "2018-04-04-13-00", "2018-04-04-13-15", "2018-04-04-13-30", "2018-04-04-13-45", "2018-04-04-14-00", "2018-04-04-14-15", "2018-04-04-14-30", "2018-04-04-14-45", "2018-04-04-15-00", "2018-04-04-15-15", "2018-04-04-15-30", "2018-04-04-15-45", "2018-04-04-16-00", "2018-04-04-16-15", "2018-04-04-16-30", "2018-04-04-16-45", "2018-04-04-17-00", "2018-04-04-17-15", "2018-04-04-17-30", "2018-04-04-17-45", "2018-04-04-18-00", "2018-04-04-18-15", "2018-04-04-18-30", "2018-04-04-18-45", "2018-04-04-19-00", "2018-04-04-19-15", "2018-04-04-19-30", "2018-04-04-19-45", "2018-04-04-20-00", "2018-04-04-20-15", "2018-04-04-20-30", "2018-04-04-20-45", "2018-04-04-21-00", "2018-04-04-21-15", "2018-04-04-21-30", "2018-04-04-21-45", "2018-04-04-22-00", "2018-04-04-22-15", "2018-04-04-22-30", "2018-04-04-22-45", "2018-04-04-23-00", "2018-04-04-23-15", "2018-04-04-23-30", "2018-04-04-23-45", "2018-04-05-00-00", "2018-04-05-00-15", "2018-04-05-00-30", "2018-04-05-00-45", "2018-04-05-01-00", "2018-04-05-01-15", "2018-04-05-01-30", "2018-04-05-01-45", "2018-04-05-02-00", "2018-04-05-02-15", "2018-04-05-02-30", "2018-04-05-02-45", "2018-04-05-03-00", "2018-04-05-03-15", "2018-04-05-03-30", "2018-04-05-03-45", "2018-04-05-04-00", "2018-04-05-04-15", "2018-04-05-04-30", "2018-04-05-04-45", "2018-04-05-05-00", "2018-04-05-05-15", "2018-04-05-05-30", "2018-04-05-05-45", "2018-04-05-06-00", "2018-04-05-06-15", "2018-04-05-06-30", "2018-04-05-06-45", "2018-04-05-07-00", "2018-04-05-07-15", "2018-04-05-07-30", "2018-04-05-07-45", "2018-04-05-08-00", "2018-04-05-08-15", "2018-04-05-08-30", "2018-04-05-08-45", "2018-04-05-09-00", "2018-04-05-09-15", "2018-04-05-09-30", "2018-04-05-09-45", "2018-04-05-10-00", "2018-04-05-10-15", "2018-04-05-10-30", "2018-04-05-10-45", "2018-04-05-11-00", "2018-04-05-11-15", "2018-04-05-11-30", "2018-04-05-11-45", "2018-04-05-12-00", "2018-04-05-12-15", "2018-04-05-12-30", "2018-04-05-12-45", "2018-04-05-13-00", "2018-04-05-13-15", "2018-04-05-13-30", "2018-04-05-13-45", "2018-04-05-14-00", "2018-04-05-14-15", "2018-04-05-14-30", "2018-04-05-14-45", "2018-04-05-15-00", "2018-04-05-15-15", "2018-04-05-15-30", "2018-04-05-15-45", "2018-04-05-16-00", "2018-04-05-16-15", "2018-04-05-16-30", "2018-04-05-16-45", "2018-04-05-17-00", "2018-04-05-17-15", "2018-04-05-17-30", "2018-04-05-17-45", "2018-04-05-18-00", "2018-04-05-18-15", "2018-04-05-18-30", "2018-04-05-18-45", "2018-04-05-19-00", "2018-04-05-19-15", "2018-04-05-19-30", "2018-04-05-19-45", "2018-04-05-20-00", "2018-04-05-20-15", "2018-04-05-20-30", "2018-04-05-20-45", "2018-04-05-21-00", "2018-04-05-21-15", "2018-04-05-21-30", "2018-04-05-21-45", "2018-04-05-22-00", "2018-04-05-22-15", "2018-04-05-22-30", "2018-04-05-22-45", "2018-04-05-23-00", "2018-04-05-23-15", "2018-04-05-23-30", "2018-04-05-23-45", "2018-04-06-00-00", "2018-04-06-00-15", "2018-04-06-00-30", "2018-04-06-00-45", "2018-04-06-01-00", "2018-04-06-01-15", "2018-04-06-01-30", "2018-04-06-01-45", "2018-04-06-02-00", "2018-04-06-02-15", "2018-04-06-02-30", "2018-04-06-02-45", "2018-04-06-03-00", "2018-04-06-03-15", "2018-04-06-03-30", "2018-04-06-03-45", "2018-04-06-04-00", "2018-04-06-04-15", "2018-04-06-04-30", "2018-04-06-04-45", "2018-04-06-05-00", "2018-04-06-05-15", "2018-04-06-05-30", "2018-04-06-05-45", "2018-04-06-06-00", "2018-04-06-06-15", "2018-04-06-06-30", "2018-04-06-06-45", "2018-04-06-07-00", "2018-04-06-07-15", "2018-04-06-07-30", "2018-04-06-07-45", "2018-04-06-08-00", "2018-04-06-08-15", "2018-04-06-08-30", "2018-04-06-08-45", "2018-04-06-09-00", "2018-04-06-09-15", "2018-04-06-09-30", "2018-04-06-09-45", "2018-04-06-10-00", "2018-04-06-10-15", "2018-04-06-10-30", "2018-04-06-10-45", "2018-04-06-11-00", "2018-04-06-11-15", "2018-04-06-11-30", "2018-04-06-11-45", "2018-04-06-12-00", "2018-04-06-12-15", "2018-04-06-12-30", "2018-04-06-12-45", "2018-04-06-13-00", "2018-04-06-13-15", "2018-04-06-13-30", "2018-04-06-13-45", "2018-04-06-14-00", "2018-04-06-14-15", "2018-04-06-14-30", "2018-04-06-14-45", "2018-04-06-15-00", "2018-04-06-15-15", "2018-04-06-15-30", "2018-04-06-15-45", "2018-04-06-16-00", "2018-04-06-16-15", "2018-04-06-16-30", "2018-04-06-16-45", "2018-04-06-17-00", "2018-04-06-17-15", "2018-04-06-17-30", "2018-04-06-17-45", "2018-04-06-18-00", "2018-04-06-18-15", "2018-04-06-18-30", "2018-04-06-18-45", "2018-04-06-19-00", "2018-04-06-19-15", "2018-04-06-19-30", "2018-04-06-19-45", "2018-04-06-20-00", "2018-04-06-20-15", "2018-04-06-20-30", "2018-04-06-20-45"
        ],
    },
    "avgs": {
        "xs": [
            "2018-03-31-12-00", "2018-04-01-12-00", "2018-04-02-12-00", "2018-04-03-12-00", "2018-04-04-12-00", "2018-04-05-12-00", "2018-04-06-12-00"
        ],

        "ys": [
            4620, 4660, 4620, 4630, 4560, 4390, 4530
        ]
    }
}