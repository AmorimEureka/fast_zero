from fast_zero.model import User


def test_create_user(session):
    user = User(username='test', email='test@test.com', password='secret')

    session.add(user)
    session.commit()

    # breakpoint()

    assert user.username == 'test'
