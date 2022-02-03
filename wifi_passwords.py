import subprocess


def extract_wifi_passwords():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('cp866').split('\n')

    profiles = [i.split(':')[1].strip() for i in profiles_data if 'Все профили пользователей' in i]

    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear')\
            .decode('cp866').split('\n')
        password = [i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i][0]
        print(f'Profile: {profile}\n'
              f'Password: {password}\n'
              f'-------------------')
        with open(file='wifi_passwords.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Profile: {profile}\n'
              f'Password: {password}\n'
              f'-------------------\n')


def main():
    extract_wifi_passwords()


if __name__ == '__main__':
    main()