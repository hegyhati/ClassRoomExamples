package rpg.view;

import rpg.model.GameStateViewer;
import rpg.presenter.Presenter;

import java.awt.Dimension;
import java.awt.Image;
import javax.swing.*;

class MapPanel extends ViewPanel{
    private final int visibilityRange;
    private final int tileSize;
    private final JLabel[][] mapView;
    private final ImageIcon WALL_ICON, FREE_ICON, MONSTER_ICON, HERO_ICON, HERO_MONSTER_ICON, FOG_ICON; 

    private ImageIcon getScaledTile(String file) {
        return new ImageIcon(new ImageIcon("resources/tiles/" + file).getImage().getScaledInstance(tileSize, tileSize, Image.SCALE_SMOOTH));
    }

    MapPanel(Presenter presenter, GameStateViewer model, int size, int visibilityRange) {
        super(presenter, model);

        this.visibilityRange = visibilityRange;
        tileSize  = size / (2*visibilityRange+1);
        mapView = new JLabel[2*visibilityRange+1][2*visibilityRange+1];
        WALL_ICON = getScaledTile("wall.png");
        FREE_ICON = getScaledTile("free.png");
        MONSTER_ICON = getScaledTile("monster.png");
        HERO_ICON = getScaledTile("hero.png");
        HERO_MONSTER_ICON = getScaledTile("heromonster.png");
        FOG_ICON = getScaledTile("fog.png");
        

        setLayout(null);
        for (int row = 0; row <  2 * visibilityRange + 1 ; ++row)
            for (int col = 0; col < 2 * visibilityRange + 1; ++col) {
                JLabel tile = new JLabel();
                tile.setBounds(tileSize*col,tileSize*row, tileSize, tileSize);
                mapView[row][col] = tile;
                add(tile);
            }
        setPreferredSize(new Dimension(size,size));

        updateView();
    }

    @Override
    public void updateView() {
         for (int row=-visibilityRange; row <= visibilityRange; ++row)
            for (int col = -visibilityRange; col <= visibilityRange; ++col) 
                mapView[row+visibilityRange][col+visibilityRange].setIcon(
                    !model.canSee(row,col)
                    ? FOG_ICON
                    : model.canSeeWall(row, col)
                        ? WALL_ICON 
                        : row == 0 && col == 0 && model.getHero().isAlive()
                            ? model.canSeeMonster(row, col) ? HERO_MONSTER_ICON : HERO_ICON
                            : model.canSeeMonster(row, col) ? MONSTER_ICON : FREE_ICON
                );
    }
}