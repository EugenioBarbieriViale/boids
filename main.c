#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <raylib.h>

#define W 1000
#define H 800

#define N 10
#define size 30

typedef struct {
    Vector2 pos;
    float vel;
    float angle;
} Boid;

void init_flock(Boid flock[]) {
    for (int i=0; i<N; i++) {
        flock[i].pos = (Vector2){i*30+200, 300};
        flock[i].angle = PI/i;
    }
}

void draw_flock(Boid flock[]) {
    for (int i=0; i<N; i++) {
        Vector2 pos = flock[i].pos;
        float a = flock[i].angle;

        Vector2 v1 = (Vector2){pos.x + size*cos(a), pos.y - size*sin(a)};
        Vector2 v2 = (Vector2){pos.x - size*sin(a)/2, pos.y - size*cos(a)/2};
        Vector2 v3 = (Vector2){pos.x + size*sin(a)/2, pos.y + size*cos(a)/2};

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
