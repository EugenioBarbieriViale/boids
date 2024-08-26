#include <stdio.h>
#include <math.h>
#include <raylib.h>

#define W 1000
#define H 800

#define N 1
#define size 30

typedef struct {
    Vector2 pos;
    float vel;
    float angle;
} Boid;

void init_flock(Boid flock[]) {
    for (int i=0; i<N; i++) {
        flock[i].pos = (Vector2){i*30+200, 300};
        flock[i].angle = PI/6;
    }
}

Vector2 rotate(Vector2 pos, float a) {
    /* float new_x = (pos.x * size * cos(a) - pos.y * size * sin(a)); */
    /* float new_y = (pos.x * size * sin(a) + pos.y * size * cos(a)); */
    float new_x = (pos.x + pos.x * cos(a) - pos.y * sin(a));
    float new_y = (pos.y + pos.x * sin(a) + pos.y * cos(a));
    return (Vector2){new_x, new_y};
}


void draw_flock(Boid flock[]) {
    for (int i=0; i<N; i++) {
        Vector2 pos = flock[i].pos;
        float a = flock[i].angle;

        /* Vector2 v1 = (Vector2){pos.x + size, pos.y}; */
        /* Vector2 v2 = (Vector2){pos.x, pos.y - (int)(size/2)}; */
        /* Vector2 v3 = (Vector2){pos.x, pos.y + (int)(size/2)}; */

        Vector2 v1 = rotate((Vector2){pos.x - size, pos.y}, a);
        Vector2 v2 = rotate((Vector2){pos.x, pos.y - (int)(size/2)}, a);
        Vector2 v3 = rotate((Vector2){pos.x, pos.y + (int)(size/2)}, a);

        DrawTriangle(v1, v2, v3, RED);
    }
}

int main() {
    InitWindow(W, H, "Boids");
    SetTargetFPS(30);

    Boid flock[N];
    init_flock(flock);

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(GRAY);

        draw_flock(flock);

        EndDrawing();

    }

    return 0;
}
