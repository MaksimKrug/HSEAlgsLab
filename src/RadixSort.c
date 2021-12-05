#include "RadixSort.h"

uint64_t get_16bit_digit(uint64_t number, uint64_t mask)
{
    uint64_t digit = number & mask;
    if (mask == mask2)
    {
        digit = digit >> 16;
    }
    else if (mask == mask3)
    {
        digit = digit >> 32;
    }
    else if (mask == mask4)
    {
        digit = digit >> 48;
    }
    return digit;
}

void counting_sort(uint64_t **p_criteria_arr, uint64_t **p_indices_arr, uint64_t len, uint64_t mask)
// Script for counting sort
{
    uint32_t *count_array = (uint32_t *)malloc(USHRT_MAX * sizeof(uint32_t));
    uint64_t *indices_array_result = (uint64_t *)malloc(len * sizeof(uint64_t));
    uint64_t *result_criteria_arr = (uint64_t *)malloc(len * sizeof(uint64_t));
    // check that malloc didn't return NULL
    if ((count_array == NULL) || (indices_array_result == NULL) || (result_criteria_arr == NULL))
    {
        exit(1);
    }

    uint64_t *criteria_arr = *p_criteria_arr;
    uint64_t *indices_arr = *p_indices_arr;

    memset(count_array, 0, USHRT_MAX * sizeof(uint32_t));
    memset(indices_array_result, 0, len * sizeof(uint64_t));
    memset(result_criteria_arr, 0, len * sizeof(uint64_t));

    for (size_t i = 0; i < len; ++i)
    {
        uint64_t digit = get_16bit_digit(criteria_arr[i], mask);
        ++count_array[digit];
    }

    for (size_t i = 1; i < USHRT_MAX; ++i)
    {
        count_array[i] += count_array[i - 1];
    }

    for (int i = len - 1; i >= 0; --i)
    {
        uint64_t digit = get_16bit_digit(criteria_arr[i], mask);
        uint64_t position = count_array[digit] - 1;
        indices_array_result[position] = indices_arr[i];
        result_criteria_arr[position] = criteria_arr[i];
        --count_array[digit];
    }

    free(indices_arr);
    free(count_array);

    *p_indices_arr = indices_array_result;
    *p_criteria_arr = result_criteria_arr;
}

uint64_t *radix_sort(uint64_t *arr, uint64_t len)
{
    uint64_t *indices = (uint64_t *)malloc(len * sizeof(uint64_t));
    // check that malloc didn't retun NULL
    if (indices == NULL)
    {
        exit(1);
    }
    for (size_t i = 0; i < len; ++i)
    {
        indices[i] = i;
    }
    // counting sort for all masks
    counting_sort(&arr, &indices, len, mask1);
    counting_sort(&arr, &indices, len, mask2);
    counting_sort(&arr, &indices, len, mask3);
    counting_sort(&arr, &indices, len, mask4);

    return indices;
}
