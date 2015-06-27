# Cyborg Secrets
拿到一個elf執行檔，是個要你輸入密碼才會給flag的程式。用vim開啟cyborg_defense收集線索：
 * 發現有一行說 debug password = 2manyHacks_Debug_Admin_Test
 * 以這個當密碼執行程式：
 ```bash
$ ./cyborg_defense 2manyHacks_Debug_Admin_Test

Password: 2manyHacks_Debug_Admin_Test
Authorization successful.
403-shutdown-for-what
```

成功取得flag = 403-shutdown-for-what
