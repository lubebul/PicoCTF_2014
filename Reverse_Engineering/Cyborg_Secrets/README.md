# Cyborg Secrets
[cyborg_defense](cyborg_defense)是個輸入密碼才會給flag的程式
 * 用vim開啟cyborg_defense收集線索：
 * 發現有一行說 `debug password = 2manyHacks_Debug_Admin_Test`
 * 取得flag

```bash
$ ./cyborg_defense 2manyHacks_Debug_Admin_Test

Password: 2manyHacks_Debug_Admin_Test
Authorization successful.
403-shutdown-for-what
```
