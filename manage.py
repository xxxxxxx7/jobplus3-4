from jobplus.app import create_app


app = create_app('defautl')


@app.cli.command()
def init_db():
    print('sqlite3数据库文件：{}'.format(app.config['SQLALCHEMY_DATABASE_URI']))

    db.create_all()


if __name__ == '__main__':
    app.run()


