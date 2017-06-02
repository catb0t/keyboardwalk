#include "../test_common/common.h"
#include <stdlib.h>
#include <inttypes.h>

/* things you can put in and get out of a matrix2d_t */
typedef enum en_mattype_t { MT_INT64, MT_CHAR, MT_UINT64 } mattype_t;

/* base descriptor for matrix objects */
typedef struct st_matrix2d_t {
  union {
     int64_t** i64data;
        char** chrdata;
    uint64_t** u64data;
  };

  /* NOTE that x and y are swapped in use order because the grid is rotated */
  uint64_t
    /* this is the horizontal position, 0 indexed; refers to an element in the 2nd array dimension (2 dereferences) */
    x,
    /* vertical position, refers to an array (1 deref) */
    y,
    /* length of current data pointer top level array */
    ylen,
    /* length, of the second array dimension (all equal) */
    *xlen;

  mattype_t dtype;

  size_t uid;
} matrix2d_t;

matrix2d_t* matrix2d_ctor (
  const void * const * const data,
  const uint64_t lx,
  const uint64_t ly,
  const mattype_t dtype,
  const uint64_t x,
  const uint64_t y
);

matrix2d_t* matrix2d_ctor (
  const void * const * const data,
  const uint64_t lx,
  const uint64_t ly,
  const mattype_t dtype,
  const uint64_t x,
  const uint64_t y
) {
  pfn(); //!!

  return NULL;
}