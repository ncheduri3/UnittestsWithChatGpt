#include <stdio.h>
#include <stdbool.h>
#include <assert.h>
#include <string.h>

#define MAX_EMAIL_LENGTH 100

int numUniqueEmails(char emails[][MAX_EMAIL_LENGTH], int emails_length) {
    int unique_count = 0;
    char unique_emails[emails_length][MAX_EMAIL_LENGTH];

    for (int i = 0; i < emails_length; i++) {
        char final_email[MAX_EMAIL_LENGTH];
        char* email = strtok(emails[i], "@");
        strcpy(final_email, email);
        char* domain = strtok(NULL, "@");

        // Remove dots from the local name
        char* p = strchr(final_email, '.');
        while (p != NULL) {
            memmove(p, p + 1, strlen(p));
            p = strchr(final_email, '.');
        }

        // Ignore everything after the first '+' sign
        p = strchr(final_email, '+');
        if (p != NULL) {
            *p = '\0';
        }

        strcat(final_email, "@");
        strcat(final_email, domain);

        bool is_duplicate = false;
        for (int j = 0; j < unique_count; j++) {
            if (strcmp(final_email, unique_emails[j]) == 0) {
                is_duplicate = true;
                break;
            }
        }

        if (!is_duplicate) {
            strcpy(unique_emails[unique_count], final_email);
            unique_count++;
        }
    }

    return unique_count;
}

void test_empty_list() {
    char emails[][MAX_EMAIL_LENGTH] = {};
    int emails_length = sizeof(emails) / sizeof(emails[0]);
    int result = numUniqueEmails(emails, emails_length);
    int expected = 0;
    assert(result == expected);
    printf("Test case 'empty_list' passed\n");
}

void test_single_email() {
    char emails[][MAX_EMAIL_LENGTH] = {"test.email@example.com"};
    int emails_length = sizeof(emails) / sizeof(emails[0]);
    int result = numUniqueEmails(emails, emails_length);
    int expected = 1;
    assert(result == expected);
    printf("Test case 'single_email' passed\n");
}

void test_duplicate_emails() {
    char emails[][MAX_EMAIL_LENGTH] = {"test.email@example.com", "test.email@example.com"};
    int emails_length = sizeof(emails) / sizeof(emails[0]);
    int result = numUniqueEmails(emails, emails_length);
    int expected = 1;
    assert(result == expected);
    printf("Test case 'duplicate_emails' passed\n");
}

void test_unique_emails() {
    char emails[][MAX_EMAIL_LENGTH] = {"test.email@example.com", "test.email2@example.com", "another.email@example.com"};
    int emails_length = sizeof(emails) / sizeof(emails[0]);
    int result = numUniqueEmails(emails, emails_length);
    int expected = 3;
    assert(result == expected);
    printf("Test case 'unique_emails' passed\n");
}

void test_emails_with_dots() {
    char emails[][MAX_EMAIL_LENGTH] = {"t.est.email@example.com", "testemail@example.com"};
    int emails_length = sizeof(emails) / sizeof(emails[0]);
    int result = numUniqueEmails(emails, emails_length);
    int expected = 1;
    assert(result == expected);
    printf("Test case 'emails_with_dots' passed\n");
}

void test_emails_with_plus() {
    char emails[][MAX_EMAIL_LENGTH] = {"test.email+spam@example.com", "test.email@example.com"};
    int emails_length = sizeof(emails) / sizeof(emails[0]);
    int result = numUniqueEmails(emails, emails_length);
    int expected = 1;
    assert(result == expected);
    printf("Test case 'emails_with_plus' passed\n");
}

void test_emails_with_com_suffix() {
    char emails[][MAX_EMAIL_LENGTH] = {"test.email@example.com", "test.email@example.org"};
    int emails_length = sizeof(emails) / sizeof(emails[0]);
    int result = numUniqueEmails(emails, emails_length);
    int expected = 2;
    assert(result == expected);
    printf("Test case 'emails_with_com_suffix' passed\n");
}

int main() {
    test_empty_list();
    test_single_email();
    test_duplicate_emails();
    test_unique_emails();
    test_emails_with_dots();
    test_emails_with_plus();
    test_emails_with_com_suffix();

    return 0;
}
